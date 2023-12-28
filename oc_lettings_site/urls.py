from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

# from . import views

urlpatterns = [
    url(r'', include('home.urls', namespace='home')),
    url(r'^lettings/', include('lettings.urls', namespace='lettings')),
    url(r'^profiles/', include('profiles.urls', namespace='profiles')),
    path('admin/', admin.site.urls),
]