from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.name}'


class Announcement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='announcements')
    name = models.CharField(max_length=128)
    # text = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='announcements')
    content = RichTextUploadingField()

    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return f'/announcement/{self.id}'


class Respond(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='responds')
    text = models.TextField(verbose_name='')
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE, related_name='announcements')
    accept = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'Answer from "{self.user.username}" to "{self.announcement.user.username}" by announcement "{self.announcement}"'