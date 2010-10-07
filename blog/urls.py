
"""
urls.py

blog urls

"""

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns("blog.views",
    url(r"^$", "index", name="index"),
)