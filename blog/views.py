
"""
  views.py

  Views for blog app
"""

from ext import template
from blog import models

def index(request):
    return template.render(request, "index.html", {
        'recent_posts': models.Post.get_recent_posts(),
    })

def details(request, year, month, slug):
    return template.render(request, "index.html", {
        'recent_posts': models.Post.get_recent_posts(),
    })