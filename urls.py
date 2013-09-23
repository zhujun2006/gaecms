from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^hello/$', 'woodchat.views.hello', name='hello'),
    url(r'^$', 'woodchat.views.index_page', name='home_default'),
    url(r'^home/$', 'woodchat.views.index_page', name='home'),
    url(r'^aboutus/$', 'woodchat.views.about_us_page', name='about_us'),
    url(r'^ourproducts/$', 'woodchat.views.our_products_page', name='our_products'),
    url(r'^contactus/$', 'woodchat.views.contact_us_page', name='contact_us'),
    # url(r'^gaecms/', include('gaecms.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
