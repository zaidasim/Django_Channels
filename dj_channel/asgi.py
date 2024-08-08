import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter 
from channels.auth import AuthMiddlewareStack
from notifications import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE','dj_channel.settings')

application=ProtocolTypeRouter({
    "https":get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
        )
    ),
})