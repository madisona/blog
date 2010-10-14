
"""
urls.py

blog urls

"""

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns("blog.views",
    url(r"^$", "index", name="index"),
    url(r"^blog/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$", "details", name="details"),

)