from django.conf.urls import include, url
from leongGoods import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'index/',views.index),
    url(r'cart/',views.cart),
    url(r'detail/',views.detail),
]
