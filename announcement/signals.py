from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Announcement
from django.conf import settings
from django.contrib.auth.models import User



@receiver(post_save, sender=Announcement)
def mailing(sender, instance, created, **kwargs):
    us = [i.email for i in User.objects.all()]
    if created:
        send_mail(f'Появилась новая запись!',
                  f'Появилась новая запись: {instance.name} от пользователя {instance.user}',
                  settings.DEFAULT_FROM_EMAIL, us)