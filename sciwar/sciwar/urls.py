from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
        url(ur'^$', 'main.views.main_page'),
        url(ur'^main', 'main.views.proto'),
        url(ur'^video', 'main.views.video_page'),
        url(ur'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
        url(r'^admin/', include(admin.site.urls)),
    # Examples:
    # url(r'^$', 'sciwar.views.home', name='home'),
    # url(r'^sciwar/', include('sciwar.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
