from django.urls import path

from . import views


def trigger_error(request):
    """Générer une erreur pour test"""
    division_by_zero = 1 / 0
    return division_by_zero


app_name = 'home'
urlpatterns = (
    path('', views.index, name='index'),
    path('error', views.error_generating, name='error'),
    path('sentry-debug/', trigger_error),
)
