from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf import settings
#from django.views.generic.simple import direct_to_template
from django.shortcuts import render

admin.autodiscover()

urlpatterns = []
if 'core' in settings.INSTALLED_APPS:
    from core.forms import RegistrationForm
    urlpatterns += patterns('',
        # url(r'^.*$', direct_to_template, {'template': 'core/maintainance.html'}),
        url(r'^$', 'core.views.main_views.home', name='home'),
       # url(r'^faq$', direct_to_template, {'template': 'core2/faq.html'}),
        url(r'^faq$', render, {'template_name': 'core2/faq.html'}),
        url(r'^core/', include('core.urls')),
        url(r'^project/', include('core.urls.project_urls')),
        url(r'^feedback', include('core.urls.feedback_urls')),
        url(r'^user/', include('core.urls.user_urls')),
        url(r'^sandbox/', include('sandbox.urls')),
        url(r'^github/', include('gh_frespo_integration.urls')),
        url(r'^bladmin/doc/', include('django.contrib.admindocs.urls')),
        url(r'^bladmin/', include(admin.site.urls)),
        url(r'^accounts/password/reset/$', 'core.views.registration_views.reset_password'),
        url(r'^/accounts/register/$', 'registration.views.register', {
            'backend': 'registration.backends.default.DefaultBackend',
            'form_class': RegistrationForm
        }, name='registration_register'),
        url(r'^accounts/', include('registration.backends.default.urls')),
        url(r'', include('social_auth.urls')),
        url(r'^email/$', 'core.views.user_views.redirect_to_user_page',
            {'email_verified': 'true'}, name='emailmgr_email_list'),
        url(r'^email/activate/(?P<identifier>\w+)/$',
            'emailmgr.views.email_activate',
            name='emailmgr_email_activate'
        ),
    )

urlpatterns += patterns('',
    url(r'^sandbox/', include('sandbox.urls')),
)

urlpatterns += staticfiles_urlpatterns()
# urlpatterns += feedback_urlpatterns
