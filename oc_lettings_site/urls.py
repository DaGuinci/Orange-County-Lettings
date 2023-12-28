from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from lettings import views as lettings_views
from profiles import views as profiles_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^lettings/', include('lettings.urls', namespace='lettings')),
    path('profiles/', profiles_views.index, name='profiles_index'),
    path('profiles/<str:username>/', profiles_views.profile, name='profile'),
    path('admin/', admin.site.urls),
]