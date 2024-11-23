from django.shortcuts import redirect, render
from django.contrib import messages
from django.urls import reverse
from .forms import RegisterForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registreerumine õnnestus!')
            return redirect('login')
        else:
            return render(request, 'users/register.html', {'form': form})
    form = RegisterForm()
    return render(request, 'users/register.html',{'form':form})

def logout_view(request):
    logout(request)
    return render(request, 'users/logout.html')

@login_required
def profilepage(request):
    return render(request, 'users/profile.html')