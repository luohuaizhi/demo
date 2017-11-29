from django.conf.urls import patterns, url
import views


urlpatterns = patterns(
        '',
        url(r'^world/$', views.hello),
        url(r'^query/(\d*)/$', views.query),
        url(r'^insert/(?P<name>\w*)/(?P<birthday>\d{4}-\d{2}-\d{2})/(?P<gender>[01])/$', views.insert),
        url(r'^delete/(?P<uid>\d*)/$', views.delete, {'is_active': False}),
        url(r'^update/(?P<name>\w*)/(?P<birthday>\w*)/$', views.update),

        url(r'^$', views.index),
        url(r'add/$', views.add),
        url(r'edit/$', views.edit),
)


