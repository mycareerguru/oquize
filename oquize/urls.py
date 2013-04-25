from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from quize.views import main_page, user_page, add_question, tag_page
from quize.views import tag_display, search_page, user_answer, result_page
from quize.views import quiz_page, like_page, unlike_page, close_page
from quize.register import logout_page, register_page, register_success
from quize.quizeview import quize_display, quize_start

urlpatterns = patterns('',
    (r'^$', main_page),
    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', logout_page),
    (r'^register/$', register_page),
    (r'^register/success/$', register_success),
    (r'^user/(\w+)/$', user_page),
    (r'^add/$', add_question),
    (r'^tags/$',tag_page),
    (r'^tags/(\w+)/$',tag_display),
    (r'^search/$', search_page),
    (r'^answer/$', user_answer),
    (r'^result/$', result_page),
    (r'^quiz/$', quiz_page),
    (r'^quiz/(\w+)/$',quize_display),
    (r'^quiz/(\w+)/start/$',quize_start),
    (r'^like/$', like_page),
    (r'^unlike/$', unlike_page),
    (r'^qclose/$', close_page),
    # Examples:
    # url(r'^$', 'oquize.views.home', name='home'),
    # url(r'^oquize/', include('oquize.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
