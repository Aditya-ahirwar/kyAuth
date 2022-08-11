from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    # path('', views.home, name = "index"),
    path('', views.signup, name = 'signup'),
    path('signup', views.signup, name = "signup"),
    path('signin', views.signin, name = 'signin'),
    path('signout', views.signout, name='signout'),
]
