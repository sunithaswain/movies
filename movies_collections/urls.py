from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='home_page'),
    url(r'^insert/', views.data_inserting, name='data_insert'),
    url(r'^all/', views.displayAll, name='display'),
    url(r'^languages/', views.language_filter, name='lan'),
    url(r'^year/', views.year_filter, name='byyear'),
    url(r'^search/', views.search_filter, name='searching'),
    url(r'^ajaxcal/', views.gettingids, name='azxcalling'),
    ] 