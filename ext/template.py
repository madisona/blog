
"""template.py

Includes some wrappers for django's templates that make them
easier to work with...
"""

from django.shortcuts import render_to_response
from django.template import RequestContext, loader

def render(req, *args, **kwargs):
    "renders the contents and makes the RequestContext available"
    kwargs['context_instance'] = RequestContext(req)
    return render_to_response(*args, **kwargs)