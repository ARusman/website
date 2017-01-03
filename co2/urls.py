from django.conf.urls import url
from .import views

app_name = 'co2'

urlpatterns = [
    # /co2/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /co2/<capital_id>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /co2/capital/add/
    url(r'capital/add/$', views.CapitalCreate.as_view(), name='capital-add'),

    # /co2/capital/2/
    url(r'capital/(?P<pk>[0-9]+)/$', views.CapitalUpdate.as_view(), name='capital-update'),

    # /co2/capital/2/delete
    url(r'capital/(?P<pk>[0-9]+)/delete$', views.CapitalDelete.as_view(), name='capital-delete'),
]