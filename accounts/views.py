from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required







# Create your views here.
from django.urls import reverse
from accounts.forms import CustomUserCreationForm
from django.contrib import messages



def register(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')
    return render(request, 'accounts/register.html', {'form': form})
    
@login_required()    
def home(request):
    return render(request, 'accounts/home.html')

def login(request):
    return render(request, 'accounts/login.html')


	
