from django.urls import path
from . import views  # Import your views

urlpatterns = [
    # Define your URL patterns here
    path('registerUser/',views.registerUser, name='registerUser'),  # Replace 'home' with an actual view function
]
