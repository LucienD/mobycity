from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class CartographyApphook(CMSApp):
    name = _("Cartography")
    urls = ["cartography.urls"]

apphook_pool.register(CartographyApphook)