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

def customerHome(request):
    
    return render(request, 'flickboutique/customerHome.html')

def businessHome(request):

    return render(request, 'flickboutique/businessHome.html')

def manageSite(request):
    
    return render(request, 'flickboutique/manageSite.html')

def productPage(request):

    return render(request, 'flickboutique/productPage.html')

def businessView(request):

    return render(request, 'flickboutique/businessView.html')