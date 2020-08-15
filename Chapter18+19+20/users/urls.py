"""Defines URL Patterns for users."""

from django.conf.urls import url
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    # Login page.
    url(r'^login/$', LoginView.as_view(template_name='users/login.html'), name='login'),

    # Logout.
    url(r'^logout/$', views.logout_view, name='logout'),

    # Register.
    url(r'^register/$', views.register, name='register'),
]
