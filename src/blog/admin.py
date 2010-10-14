
from django import forms
from django.contrib import admin
from django.contrib.admin import widgets

from blog import models

class AdminPostForm(forms.ModelForm):
    
    class Meta:
        model = models.Post
        exclude = ('slug', 'body_html')
        widgets = {
            'publish_date': widgets.AdminDateWidget(format="%m/%d/%Y"),
        }

class AdminPost(admin.ModelAdmin):
    form = AdminPostForm

admin.site.register(models.Post, AdminPost)

