from django.shortcuts import render


def index(request):
    return render(request, 'home/index.html')

def custom_404(request, exception):
    return render(request, 'home/404.html')

def custom_500(request):
    return render(request, 'home/500.html')

def error_generating(request):
    raise Exception("This is a test error")