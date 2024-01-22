from django.shortcuts import render
from lettings.models import Letting
from django.core.exceptions import ObjectDoesNotExist
import sentry_sdk


def index(request):
    """
    Affiche la liste des lettings
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """
    Affiche les détails d'un letting
    """
    try:
        letting = Letting.objects.get(id=letting_id)
        context = {
                'title': letting.title,
                'address': letting.address,
            }
        return render(request, 'lettings/letting.html', context)
    except ObjectDoesNotExist:
        sentry_sdk.capture_message("Letting not found")
        context = {'type': 'letting'}
        return render(request, 'home/404.html', context)
