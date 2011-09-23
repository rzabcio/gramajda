from django.conf.urls.defaults import *

from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib.auth.views import login,logout
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from grajteka.views import *

admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^gramajda/', include('gramajda.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    #(r'^admin/(.*)', include(admin.site.root)),

    (r'^/?$', 'grajteka.views.index'),
    (r'^/?accounts/$', lambda x:HttpResponseRedirect('/')),
    (r'^/?accounts/profile/$', lambda x:HttpResponseRedirect('/')),
    (r'^/?accounts/login/$', login),
    (r'^/?accounts/logout/$', logout),
    (r'^/?user/(?P<username>\w+)/$', 'grajteka.views.user_view'),
    (r'^/?user/$', 'grajteka.views.users_all'),
	(r'^/?(?P<json>json/)?boardgames_list/$', 'grajteka.views.boardgames_list'),
    (r'^/?(?P<json>json/)?boardgames/$', 'grajteka.views.boardgames'),
    (r'^/?boardgame/(?P<boardgameid>\d+)/$', 'grajteka.views.boardgame_view'),
    (r'^/?boardgame/transfer/$', 'grajteka.views.boardgame_transfer'),

    (r'^/?event/$', 'grajteka.views.event_view'),
    (r'^/?event_change/$', 'grajteka.views.event_change_view'),
	(r'^/?event_set/(?P<eventid>\d+)/$', 'grajteka.views.event_set'),

	#(r'^/?json/boardgames_list/$', 'grajteka.jsons.boardgames_list'),

	(r'^/?poligon/$', 'grajteka.views.poligon'),
)

if settings.DEBUG:
	urlpatterns += staticfiles_urlpatterns()
