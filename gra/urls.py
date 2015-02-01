from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


from main.views import player_list, register_page
from main.views import login_page, index, logout_page, panel, widok_miasta
from main.views import koszary_ludzi, koszary_goblinow, uniwersytet, prorok


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gra.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index),

    url(r'^players/$', player_list),

    url(r'^register/$', register_page),

    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$',logout_page),

    url(r'^panel/$', panel),
    url(r'^widok_miasta/$', widok_miasta),

    url(r'^koszary_ludzi/',koszary_ludzi),
    url(r'^koszary_goblinow/',koszary_goblinow),

    url(r'^uniwersytet/', uniwersytet),
    url(r'^prorok/',prorok),

)
