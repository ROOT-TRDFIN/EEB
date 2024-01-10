"""
URL configuration for EEBEDCS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from EEBapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name="contact"),
    path('product/',views.product,name='product'),
    path('domeindex/',views.domeindex,name='domeindex'),
    path('domeabout/',views.domeabout,name='domeabout'),
    path('domeblog/',views.domeblog,name='domeblog'),
    path('domecontact/',views.domecontact,name='domecontact'),
    path('domeservices/',views.domeservices,name='domeservices'),
    path('ampibious/',views.ampibious,name='ampibious'),
    path('autoindex/',views.autoindex,name='autoindex'),
    path('autoportfolio/',views.autoportfolio,name='autoportfolio'),
    path('autoabout/',views.autoabout,name='autoabout'),
    path('autocontact/',views.autocontact,name='autocontact'),
    path('hydro/',views.hydro,name='hydro'),
    path('scafolding/',views.scafolding,name='scafolding'),
    path('floatation/',views.floatation,name='floatation')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)