from django.conf.urls import patterns, url
from django.shortcuts import render

__author__ = 'tony'

urlpatterns = patterns('sandbox.views',
    url(r'^$', 'home'),
    url(r'^issue$', 'issue'),
    url(r'^project_edit', render, {'template': 'core2/project_edit.html'}),
    url(r'^project', 'project'),
    # url(r'^project_page$', direct_to_template, {'template': 'sandbox/project.html'}),
    url(r'^faq$', render, {'template': 'core2/faq.html'}),
    url(r'^user_page$', render, {'template': 'sandbox/user.html'}),
	url(r'^search_page$', render, {'template': 'sandbox/search.html'}),
    url(r'^adropdown', render, {'template': 'sandbox/adropdown.html'}),
    url(r'^atabnav', render, {'template': 'sandbox/atabnav.html'}),
    url(r'^amodal', render, {'template': 'sandbox/amodal.html'}),
    url(r'^apopover', render, {'template': 'sandbox/apopover.html'}),
)

