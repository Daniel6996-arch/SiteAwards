from django.conf import settings
from django.conf.urls import url
from django.urls import path
from . import views
from .views import WebsiteListView, ProfileView, ProfileEditView, WebsiteDetailView, UserList, SiteList, Usability, Design, Content

urlpatterns = [
    url('^$', views.index, name  = 'index'),
    url('site_of_day/', WebsiteListView.as_view(), name='site_of_day'),
    #url(r'^ajax/newsletter/$', views.newsletter, name='newsletter'),
    url('^profile/(?P<pk>\d+)/$', ProfileView.as_view(), name = 'profile'),
    url('^profile/edit/(?P<pk>\d+)/$', ProfileEditView.as_view(), name = 'profile-edit'),
    url('^post/(?P<pk>\d+)/$', WebsiteDetailView.as_view(), name = 'website-detail'),
    url('^search/',views.search,name='search'),
    url(r'^api/users/$', views.UserList.as_view()),
    url(r'^api/projects/$', views.SiteList.as_view()),
    url('^site/usability/(?P<pk>\d+)/$', Usability.as_view(), name = 'usability'),
    url('^site/design/(?P<pk>\d+)/$', Design.as_view(), name = 'design'),
    url('^site/content/(?P<pk>\d+)/$', Content.as_view(), name = 'content'),
]    