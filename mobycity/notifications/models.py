from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Notification(models.Model):
    creation_datetime = models.DateTimeField(blank=True, default=timezone.now)
    update_datetime = models.DateTimeField(blank=True, default=timezone.now)

    recipient = models.ForeignKey(User)

    read = models.BooleanField(default=False)
    content = models.CharField(max_length=255)