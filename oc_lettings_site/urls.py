from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from lettings import views as lettings_views
from profiles import views as profiles_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^lettings/', include('lettings.urls', namespace='lettings')),
    url(r'^profiles/', include('profiles.urls', namespace='profiles')),
    path('admin/', admin.site.urls),
]