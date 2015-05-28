from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render

# Create your views here.

def home(request):
    form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'home.html', context=context)
