from django.urls import path

import mainpage
from mainpage import views

urlpatterns = [

    path('', views.index, name = 'home'),
    path('about-us', views.about, name = 'about'),
    path('create', views.create, name='create'),
]