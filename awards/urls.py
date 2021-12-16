from django.conf import settings
from django.conf.urls import url
from django.urls import path
from . import views
from .views import WebsiteListView, ProfileView, ProfileEditView, WebsiteDetailView

urlpatterns = [
    url('^$', views.index, name  = 'index'),
    url('site_of_day/', WebsiteListView.as_view(), name='site_of_day'),
    url('^profile/(?P<pk>\d+)/$', ProfileView.as_view(), name = 'profile'),
    url('^profile/edit/(?P<pk>\d+)/$', ProfileEditView.as_view(), name = 'profile-edit'),
    url('^post/(?P<pk>\d+)/$', WebsiteDetailView.as_view(), name = 'website-detail'),
]    