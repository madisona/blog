
from django.http import HttpResponse
from django.template import loader, RequestContext

from wmd import settings as wmd_settings

def wmd_settings_js(request):
    template_files = (
        'wmd-settings.js',
    )

    template = loader.select_template(template_files)

    settings = {
        'WMD_OUTPUT' : wmd_settings.WMD_OUTPUT,
        'WMD_LINE_LENGTH': wmd_settings.WMD_LINE_LENGTH,
        'WMD_BUTTONS' : wmd_settings.WMD_BUTTONS,
    }

    context = RequestContext(request, settings )
    return HttpResponse(template.render(context),
            content_type="application/x-javascript")

def wmd_css(request):
    template_files = (
        'wmd.css',
    )
    template = loader.select_template(template_files)

    context = RequestContext(request)
    
    return HttpResponse(template.render(context), content_type="text/css")