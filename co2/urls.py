from django.conf.urls import url
from .import views

urlpatterns = [
    # /co2/
    url(r'^$', views.index, name='index'),

    # /co2/<the id>/
    url(r'^(?P<capital_id>[0-9]+)/$', views.detail, name='detail'),
]