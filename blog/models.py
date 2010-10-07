
import datetime
import markdown

from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

from wmd import models as wmd_models

class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)
    body_text = wmd_models.MarkDownField()
    body_html = models.TextField()
    active = models.BooleanField(default=True)
    allow_comment = models.BooleanField(default=True)
    publish_date = models.DateField(default=datetime.date.today)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.body_html = markdown.markdown(self.body_text)
        super(Post, self).save(*args, **kwargs)