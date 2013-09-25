from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
        url(ur'^$', 'main.views.main_page'),
        url(ur'^info/$', 'main.views.info_page'),
        url(ur'^schedule/$', 'main.views.schedule_page'),
        url(ur'^map/$', 'main.views.map_page'),
        url(ur'^video/$', 'main.views.video_page'),

        url(ur'^info/update/$', 'main.views.update_information'),
        url(ur'^video/update/$', 'main.views.update_video'),

        # For media files to be uploaded
        url(ur'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

        # Admin page
        url(r'^admin/', include(admin.site.urls)),
)
