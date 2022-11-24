
from django.contrib import admin
from django.urls import path, include

import mainpage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainpage.urls')),
]
