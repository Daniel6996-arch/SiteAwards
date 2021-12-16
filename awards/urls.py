from django.conf import settings
from django.conf.urls import url
from . import views
from .views import WebsiteListView

urlpatterns = [
    url('^$', views.index, name  = 'index'),
    url('site_of_day/', WebsiteListView.as_view(), name='site_of_day'),
]    