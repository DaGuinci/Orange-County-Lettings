from django.shortcuts import render
from .models import Profile
from django.core.exceptions import ObjectDoesNotExist
import sentry_sdk


def index(request):
    """
    Affiche la liste des profiles
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """
    Affiche les détails d'un profile
    """
    try:
        profile = Profile.objects.get(user__username=username)
        context = {'profile': profile}
        return render(request, 'profiles/profile.html', context)
    except ObjectDoesNotExist:
        sentry_sdk.capture_message("Profile not found")
        context = {'type': 'profile'}
        return render(request, 'home/404.html', context, status=404)
