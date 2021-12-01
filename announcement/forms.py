from django.forms import ModelForm
from .models import Announcement, Respond


class AnnouncementForm(ModelForm):
    class Meta:
        model = Announcement
        fields = ['name', 'category', 'content', ]


class RespondForm(ModelForm):
    class Meta:
        model = Respond
        fields = ['text']
