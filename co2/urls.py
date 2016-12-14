from django.conf.urls import url
from .import views

app_name = 'co2'

urlpatterns = [
    # /co2/
    url(r'^$', views.index, name='index'),

    # /co2/<capital_id>/
    url(r'^(?P<capital_id>[0-9]+)/$', views.detail, name='detail'),

    # /co2/<capital_id>/favorite/
    url(r'^(?P<capital_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
]