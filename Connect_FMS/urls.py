from django.conf.urls import patterns, include, url
from django.contrib import adminfrom Connect_FMS import views

urlpatterns = patterns('',
    url(r'^$', views.home),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name':'login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^buy/$', views.buy, name='buy'),
    url(r'^sell/$', views.sell, name='sell'),
    url(r'^selling/$', views.selling, name='selling'),
    url(r'^search/$', views.search, name='search'),
    url(r'^profile/(?P<id>\d+)$', views.profile, name='profile'),
    url(r'^my_account/$', views.my_account, name='my_account'),
    url(r'^rate_user/(?P<id>\d+)/(?P<rating>\d+)$', views.rate_user, name='rate'),
    url(r'^comment/(?P<id>\d+)$', views.comment_on_user, name='comment'),
    url(r'^rate_user/$', views.rate_user, name='rate_user'),
    url(r'^edit_sale/(?P<id>\d+)$', views.edit_sale, name='edit_sale'),
    url(r'^delete_item/(?P<id>\d+)$', views.delete_item, name='delete_item'),
    url(r'^slash_price/(?P<id>\d+)/(?P<amt>\d+)$', views.slash_price, name='slash_price'),
    url(r'^avatar/(?P<id>\d+)$', views.get_avatar, name='avatar'),
    url(r'^picture/(?P<id>\d+)$', views.get_picture, name='picture'),
    url(r'^category/([a-z]+)$', views.category, name='category'),
    url(r'^change_password/$', views.change_password, name='change_password'),
    url(r'^forgotpassword/$', views.forgotpassword, name='forgot'),
    url(r'^resetpassword/$', views.resetpassword, name='reset'),
    url(r'^resetpassword-confirm/(?P<username>[a-zA-Z0-9_@\+\-]+)/(?P<token>[a-z0-9\-]+)$', views.resetpassword_confirm, name='reset-confirm'),
    url(r'^resetpassword-check/(?P<username>[a-zA-Z0-9_@\+\-]+)$', views.resetpassword_check, name='reset-check'),
    url(r'^confirm-registration/(?P<username>[a-zA-Z0-9_@\+\-]+)/(?P<token>[a-z0-9\-]+)$', views.confirm_registration, name='confirm'),
)




"""

from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'potluck.views.home'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name':'login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
    url(r'^register/$', 'potluck.views.register', name='register'),
    url(r'^buy/$', 'potluck.views.buy', name='buy'),
    url(r'^sell/$', 'potluck.views.sell', name='sell'),
    url(r'^selling/$', 'potluck.views.selling', name='selling'),
    url(r'^search/$', 'potluck.views.search', name='search'),
    url(r'^profile/(?P<id>\d+)$', 'potluck.views.profile', name='profile'),
    url(r'^my_account/$', 'potluck.views.my_account', name='my_account'),
    url(r'^rate_user/(?P<id>\d+)/(?P<rating>\d+)$', 'potluck.views.rate_user', name='rate'),
    url(r'^comment/(?P<id>\d+)$', 'potluck.views.comment_on_user', name='comment'),
    url(r'^rate_user/$', 'potluck.views.rate_user', name='rate_user'),
    url(r'^edit_sale/(?P<id>\d+)$', 'potluck.views.edit_sale', name='edit_sale'),
    url(r'^delete_item/(?P<id>\d+)$', 'potluck.views.delete_item', name='delete_item'),
    url(r'^slash_price/(?P<id>\d+)/(?P<amt>\d+)$', 'potluck.views.slash_price', name='slash_price'),
    url(r'^avatar/(?P<id>\d+)$', 'potluck.views.get_avatar', name='avatar'),
    url(r'^picture/(?P<id>\d+)$', 'potluck.views.get_picture', name='picture'),
    url(r'^category/([a-z]+)$', 'potluck.views.category', name='category'),
    url(r'^change_password/$', 'potluck.views.change_password', name='change_password'),
    url(r'^forgotpassword/$', 'potluck.views.forgotpassword', name='forgot'),
    url(r'^resetpassword/$', 'potluck.views.resetpassword', name='reset'),
    url(r'^resetpassword-confirm/(?P<username>[a-zA-Z0-9_@\+\-]+)/(?P<token>[a-z0-9\-]+)$', 'potluck.views.resetpassword_confirm', name='reset-confirm'),
    url(r'^resetpassword-check/(?P<username>[a-zA-Z0-9_@\+\-]+)$', 'potluck.views.resetpassword_check', name='reset-check'),
    url(r'^confirm-registration/(?P<username>[a-zA-Z0-9_@\+\-]+)/(?P<token>[a-z0-9\-]+)$', 'potluck.views.confirm_registration', name='confirm'),
)
"""