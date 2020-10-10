from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required







# Create your views here.
from django.urls import reverse
from accounts.forms import CustomUserCreationForm



def register(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('register'))
    return render(request, 'accounts/register.html', {'form': form})
    
@login_required()    
def home(request):
    return render(request, 'accounts/home.html')

def login(request):
    return render(request, 'accounts/login.html')


	
