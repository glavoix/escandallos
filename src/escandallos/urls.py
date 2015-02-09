from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'escandallos.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^about-us/$', 'providermgr.views.aboutus', name='aboutus'),
    url(r'^$', 'providermgr.views.home', name='home'),
    url(r'^addproduct/$', 'providermgr.views.addproduct', name='addproduct'),
    url(r'^listproducts/$', 'providermgr.views.listproducts', name='listproducts'),
    url(r'^ivatype/$', 'providermgr.views.ivatype', name='ivatype'),
    url(r'^addrecipe/$', 'providermgr.views.addrecipe', name='addrecipe'),
    url(r'^admin/', include(admin.site.urls)),


)

