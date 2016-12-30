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
]