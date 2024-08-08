# myapp/utils.py


from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

def send_notifications(user_id, message):
    from .models import Notification
    try:
        user = User.objects.get(pk=user_id)
        Notification.objects.create(user=user, message=message)
    except ObjectDoesNotExist:
        print(f"User with ID {user_id} does not exist.")
