from django.shortcuts import render
from .models import Profile
from django.shortcuts import get_object_or_404


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
    profile = get_object_or_404(Profile, user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
