# myapp/views.py

from django.shortcuts import render
from .models import Notification
from .utils import send_notifications

def some_view(request):
    send_notifications(user_id=1, message='This is a notification')
    notifications = Notification.objects.filter(user_id=1).order_by('-timestamp')
    return render(request, 'notifications/templates/notifications/notification_list.html', {'notifications': notifications})
