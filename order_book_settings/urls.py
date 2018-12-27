from django.conf.urls import include, url
from django.contrib import admin
# from django.urls import path
from home.views import index
from django.conf import settings
from django.conf.urls.static import static
from django.views import static
from turkey_orders import urls as turkey_orders_urls
from turkey_orders.views import turkey_order_list, new_turkey_order


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index, name='index'),
    url(r'', include(turkey_orders_urls)),
    # url(r'^$', base, name='base'),
]
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)