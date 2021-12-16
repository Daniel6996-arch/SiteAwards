from django.conf import settings
from django.conf.urls import url
from django.urls import path
from . import views
from .views import WebsiteListView

urlpatterns = [
    url('^$', views.index, name  = 'index'),
    url('site_of_day/', WebsiteListView.as_view(), name='site_of_day'),
    path('^profile/<int:pk>/', ProfileView.as_view(), name = 'profile'),
]    