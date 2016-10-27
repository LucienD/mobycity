from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class CarpoolingApphook(CMSApp):
    name = _("Carpooling")
    urls = ["carpooling.urls"]

apphook_pool.register(CarpoolingApphook)