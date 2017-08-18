from __future__ import unicode_literals

from .utils import get_site_settings_from_request


def settings(request):
    # type: (django.http.request.HttpRequest) -> dict
    """Returns site settings which can be accessed with 'settings' key."""
    return {'settings': get_site_settings_from_request(request)}

def whitelabel_processor(request):
    current_domain = request.get_host() 
    whitelabel = Whitelabel.objects.filter(primary_domain=current_domain).order_by('id')

    if whitelabel.count() != 0:
        config = {
            'SITE_NAME': whitelabel[0].name, 
            'SITE_LOGO': whitelabel[0].logo, 
            'SITE_DOMAIN': whitelabel[0].primary_domain
            }
    else:
        config = {
            'SITE_NAME': 'MY SITE', 
            'SITE_LOGO': '/static/images/logo.png', 
            'SITE_DOMAIN': 'http://%s' % Site.objects.get_current().domain
            }

    return config
