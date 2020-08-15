from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm


def logout_view(request):
    """User logout."""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))


def register(request):
    """User register"""
    if request.method != 'POST':
        # Show empty form
        form = UserCreationForm()
    else:
        # Deal with existing form.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # User auto login, then redirect to home page.
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))

    context = {'form': form}
    return render(request, 'users/register.html', context)
