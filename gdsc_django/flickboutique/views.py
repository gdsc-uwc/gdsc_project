from django.shortcuts import render
from django.http import HttpResponse
from . import forms

# Create your views here.

def index(request):
    return render(request, 'flickboutique/layout.html')

def customerSignup(request):

    form = forms.CustomerSignupForm()

    context = {
        'form' : form,
    }

    return render(request, 'flickboutique/customerSignup.html', context)

def businessSignup(request):

    form = forms.BusinessSignupForm()

    context = {
        'form' : form,
    }

    return render(request, 'flickboutique/businessSignup.html', context)

def customerLogin(request):

    form = forms.CustomerLoginForm()

    context = {
        'form' : form,
    }
    return render(request, 'flickboutique/customerLogin.html', context)

def businessLogin(request):

    form = forms.BusinessLoginForm()

    context = {
        'form' : form,
    }
    return render(request, 'flickboutique/businessLogin.html', context)

def userHome(request):
    return render(request, 'flickboutique/userHome.html')

def businessHome(request):
    return render(request, 'flickboutique/businessHome.html')