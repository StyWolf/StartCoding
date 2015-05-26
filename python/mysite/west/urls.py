#coding=utf8

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
		url(r'^$','west.views.first_page'),
		url(r'^staff/','west.views.staff'),
		url(r'^sec/$','west.views.sec_page'),
		url(r'^templay/$','west.views.templay'),
		url(r'^staffsec','west.views.staff_sec'),
		url(r'^form','west.views.form'),
		url(r'^rkt','west.views.rkt'),
		url(r'^post/','west.views.post_form'),
	)

