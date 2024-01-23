from django.shortcuts import render
import sentry_sdk
# from django.shortcuts import render_to_response
# from django.template import RequestContext


def index(request):
    """
    Affiche la page d'accueil du site
    """
    return render(request, 'home/index.html')


def custom_404(request, exception):
    """
    Affiche la page 404 personnalisée
    """
    sentry_sdk.capture_message("Custom 404 error")
    return render(request, 'home/404.html', status=404)


def custom_500(request):
    """
    Affiche la page 500 personnalisée
    """
    return render(request, 'home/500.html')


def error_generating(request):
    """
    Génère une erreur pour test de la page 500
    """
    try:
        '2' + 2
    except TypeError:
        sentry_sdk.capture_message("Custom test error")
        return render(request, 'home/500.html', status=500)
