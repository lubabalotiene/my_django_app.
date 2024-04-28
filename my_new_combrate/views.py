from django.shortcuts import render

# Create your views here.
# my_new_combrate/views.py
from django.shortcuts import render
from .models import my_new_combrate


def home_view(request):
    combrate_variable = my_new_combrate.objects.all()
    return render(request, 'home.html', {'my_new_combrate': combrate_variable})

def my_new_combrate_details(request, my_new_combrate_id):
    combrate_variable = my_new_combrate.objects.get(id=my_new_combrate_id)
    return render(request, 'my_new_combrate_details.html', {'my_new_combrate': combrate_variable})

def about_view(request):
    combrate_variable = my_new_combrate.objects.all() 
    return render(request, 'about.html', {'my_new_combrate': combrate_variable})

# to take the user to the login page
def user_login(request):
    return render(request, 'authentication/login.html')
