from __future__ import unicode_literals
from .utils import get_cart_from_request
from ..site.models import Whitelabel
from django.contrib.sites.models import Site


def cart_counter(request):
    """ Return number of items from cart """
    cart = get_cart_from_request(request)
    return {'cart_counter': cart.quantity}

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
            'SITE_NAME': 'GetVitaminLab', 
            'SITE_LOGO': 'images/saleor_logo.svg', 
            'SITE_DOMAIN': 'http://%s' % Site.objects.get_current().domain
            }

    return config
