from django.urls import path
from . import views

urlpatterns = [
    
    path('notifications/',views.some_view,name='notification_list')
]
