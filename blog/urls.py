from django.urls import path
from .views import renderRegisterForm,renderLoginForm,renderHomePage


urlpatterns = [
    path('',renderHomePage),
    path('register', renderRegisterForm),
    path('login', renderLoginForm)
]