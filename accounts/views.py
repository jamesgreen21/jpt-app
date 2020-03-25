from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .forms import (
    UserRegisterForm,
    UserUpdateForm,
    ProfileRegisterForm,
)


def register(request):
    """
    Returns a view that renders the register page and form
    """
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST, instance=request.user)
        profile_form = ProfileRegisterForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Registration complete. Let the fun begin!')
    else:
        user_form = UserRegisterForm()
        profile_form = ProfileRegisterForm()

    context = {
        'title': 'Register',
        'nbar': 'register',
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'register.html', context)


@login_required
def profile(request):
    """
    Returns a view that renders the profile page and form
    """
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileRegisterForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been successfully updated.')
            return redirect('user-profile')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileRegisterForm(instance=request.user.profile)

    context = {
        'title': 'Profile',
        'nbar': 'profile',
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, 'profile.html', context)


def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('password_change')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'password_change_form.html', {
        'form': form
    })