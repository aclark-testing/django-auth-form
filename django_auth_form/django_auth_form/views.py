from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as _login
from django.contrib.auth import logout as _logout
from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            _login(request, form.get_user())
            return HttpResponseRedirect("/")
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'home.html', context=context)

def logout(request):
    _logout(request)
    return HttpResponseRedirect("/")
