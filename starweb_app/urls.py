from django.urls import path
from .views import index_view,products_view,accept_cookies,reject_cookies,cookie_policy


urlpatterns = [
    path('',index_view,name='index-view'),
    path('products/', products_view, name='products-view'),
    path('accept-cookies/', accept_cookies, name='accept_cookies'),
    path('reject-cookies/', reject_cookies, name='reject_cookies'),
    path('cookie-policy/', cookie_policy, name='cookie_policy'),
]
