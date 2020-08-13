from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import logout


def logout_view(request):
    """User logout."""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))
