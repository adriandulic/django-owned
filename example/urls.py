from django.conf.urls.defaults import *
from notes.models import Note

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$',
        'owned.generic.owned_object_list',
        dict(queryset=Note.objects.all()),
        name='list_notes'),
    url(r'^view/(?P<object_id>\d+)/?$',
        'owned.generic.owned_object_detail',
        dict(queryset=Note.objects.all()),
        name='view_note'),
    
    # Example:
    # (r'^django_owned_app/', include('django_owned_app.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
