
"""
  views.py

  Views for blog app
"""

import datetime

from django import shortcuts

from ext import template
from blog import models

def index(request):
    return template.render(request, "index.html", {
        'recent_posts': models.Post.get_recent_posts(),
    })

def details(request, year, month, day, slug):
    post_date = datetime.date(int(year), int(month), int(day))
    post = shortcuts.get_object_or_404(models.Post, publish_date=post_date, slug=slug)

    return template.render(request, "detail.html", {
        'post': post,
        'comments': "",
    })