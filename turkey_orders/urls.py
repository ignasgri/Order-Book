from django.conf.urls import url
from turkey_orders.views import *


urlpatterns = [
   
    url(r'^(?P<id>\d+)/$', turkey_order_detail, name='turkey_order_detail'),
    url(r'^turkey_order/(?P<id>\d+)/edit$', edit_turkey_order, name='edit_turkey_order'),
    url(r'^turkey_order/new/$', new_turkey_order, name='new_turkey_order'),
    url(r'^all_turkey_orders$', turkey_order_list, name='turkey_order_list'),
]