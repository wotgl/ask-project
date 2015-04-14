__author__ = 'sasha1003'

from django.contrib import admin
from django.conf.urls import patterns, include, url

from core.views import index, popular, question, tag, signup, login, base, ask, paginator

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', index, name='index'),
	url(r'^popular/', popular, name='popular'),
	url(r'^question/(?P<question_id>\d+)/$', question, name='question'),
	url(r'^tag/(?P<tag_name>\w+)/$', tag, name='tag'),
	url(r'^signup/', signup, name='signup'),
	url(r'^login/', login, name='login'),
	url(r'^base/', base, name='base'),
	url(r'^ask/', ask, name='ask'),
)

