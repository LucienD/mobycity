from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from user_profile.forms import PictureForm, PhoneForm
from user_profile.models import UserProfile


@login_required
def index(request):
    context = {
        
    }
    
    return render(request, 'user_profile/index.html', context)


@login_required
def change_picture(request):
    # Deja un profil
    try:
        instance = UserProfile.objects.get(user=request.user)
    # Creation profil
    except UserProfile.DoesNotExist:
        instance = UserProfile(user=request.user)
    
    form = PictureForm(request.POST or None, request.FILES, instance=instance, initial={'picture':instance.picture})
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile picture has been changed.')
            return HttpResponseRedirect('')
        else:
            messages.error(request, 'An error happened.')
    
    context = {
        'form': form,
    }
    
    return render(request, 'user_profile/change_picture.html', context)


@login_required
def change_phone(request):
    # Deja un profil
    try:
        instance = UserProfile.objects.get(user=request.user)
    # Creation profil
    except UserProfile.DoesNotExist:
        instance = UserProfile(user=request.user)
    
    form = PhoneForm(request.POST or None, instance=instance, initial={'phone':instance.phone})
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Your phone number has been changed.')
            return HttpResponseRedirect('')
        else:
            messages.error(request, 'An error happened.')
    
    context = {
        'form': form,
    }
    
    return render(request, 'user_profile/change_phone.html', context)