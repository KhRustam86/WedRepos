"""
Definition of urls for DjangoWeb1.
"""

from datetime import datetime
from django.urls import path
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('anketa/', views.anketa, name='anketa'),
    path('regest/', views.regest, name='regest'),
    path('^(?P<parametr>\d+)/$', views.blogpost, name='blogpost'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]
