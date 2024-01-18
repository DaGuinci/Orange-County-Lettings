from django.shortcuts import render
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
    raise Exception("This is a test error")
