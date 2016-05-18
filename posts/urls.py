from django.conf.urls import url

from . import views

app_name = 'posts'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<post_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^register/$', views.RegistrationView.as_view(), name='register'),
    url(r'^login/$', views.log_in, name='login'),
    url(r'^logout/$', views.log_out, name='logout'),
    url(r'^post/$', views.post, name='post'),
    url(r'^(?P<post_id>[0-9]+)/comment/$', views.comment, name='comment'),
]