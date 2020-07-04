from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash


# Create your views here.

def index(request):
    return render(request, 'homepage/index.html')


def RegisterUser(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')

    else:
        form = UserCreationForm()

        return render(request, 'registration/register_form.html', {'form': form})


@login_required(login_url='/login')
def UserProfileView(request):
    current_user = UserProfile.objects.filter(user_id=request.user.id)
    return render(request, 'profile/profile.html', {'user': current_user})


@login_required(login_url='/login')
def ChangePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/login')
        else:
            return redirect('/login')

    else:
        form = PasswordChangeForm(user=request.user)
        return render(request, 'registration/changepassword.html', {'form': form})
