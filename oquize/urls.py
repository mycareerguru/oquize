from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from quize.views import main_page, user_page, add_question
from quize.register import logout_page, register_page, register_success

urlpatterns = patterns('',
    (r'^$', main_page),
    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', logout_page),
    (r'^register/$', register_page),
    (r'^register/success/$', register_success),
    (r'^user/(\w+)/$', user_page),
    (r'^add/$', add_question)
    # Examples:
    # url(r'^$', 'oquize.views.home', name='home'),
    # url(r'^oquize/', include('oquize.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
