from django.contrib import admin
from .models import Announcement, Category, Respond
from ckeditor_uploader.widgets import CKEditorUploadingWidget

# admin.site.register(Announcement)
admin.site.register(Category)
admin.site.register(Respond)

from django import forms
from ckeditor.widgets import CKEditorWidget


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Announcement
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm


admin.site.register(Announcement, PostAdmin)
