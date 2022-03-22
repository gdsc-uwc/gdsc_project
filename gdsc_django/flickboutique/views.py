from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from . import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from . import models

# Create your views here.

def index(request):
    return render(request, 'flickboutique/landingPage.html')


def customerSignup(request):

    form = forms.CustomerSignupForm()

    if request.method == 'POST':
        
        submittedForm = forms.CustomerSignupForm(request.POST)

        if submittedForm.is_valid():

            firstName = submittedForm.cleaned_data['firstName']
            lastName = submittedForm.cleaned_data['lastName']
            userName = submittedForm.cleaned_data['userName']
            email = submittedForm.cleaned_data['email']
            birthday = submittedForm.cleaned_data['birthday']
            streetAddress = submittedForm.cleaned_data['streetAddress']
            city = submittedForm.cleaned_data['city']
            suburb = submittedForm.cleaned_data['suburb']
            postalCode = submittedForm.cleaned_data['postalCode']
            country = submittedForm.cleaned_data['country']
            phoneNumber = submittedForm.cleaned_data['phoneNumber']
            password = submittedForm.cleaned_data['password']
            confirmPassword = submittedForm.cleaned_data['confirmPassword']

            if (password == confirmPassword):
                # User authentication creation
                user = User.objects.create_user(first_name=firstName, last_name=lastName, username=userName, email=email, password=password)
                user.save()

                # Other information saved to database
                userInfo = models.CustomerInfo(user=user, streetAddress=streetAddress, birthday=birthday, city=city, country=country, suburb=suburb, postalCode=postalCode, phoneNumber=phoneNumber)
                userInfo.save()

                return HttpResponseRedirect(reverse('flickboutique:customerSignupSuccess'))

    context = {
        'form' : form,
    }

    return render(request, 'flickboutique/customerSignup.html', context)


def customerSignupSuccess(request):
    return render(request, 'flickboutique/customerSignupSuccess.html')


def businessSignupSuccess(request):
    return render(request, 'flickboutique/businessSignupSuccess.html')


def businessSignup(request):

    form = forms.BusinessSignupForm()

    if request.method == 'POST':
        
        submittedForm = forms.BusinessSignupForm(request.POST)

        if submittedForm.is_valid():

            businessName = submittedForm.cleaned_data['businessName']
            userName = submittedForm.cleaned_data['userName']
            email = submittedForm.cleaned_data['email']
            streetAddress = submittedForm.cleaned_data['streetAddress']
            city = submittedForm.cleaned_data['city']
            suburb = submittedForm.cleaned_data['suburb']
            postalCode = submittedForm.cleaned_data['postalCode']
            country = submittedForm.cleaned_data['country']
            contactNumber = submittedForm.cleaned_data['contactNumber']
            password = submittedForm.cleaned_data['password']
            confirmPassword = submittedForm.cleaned_data['confirmPassword']

            if (password == confirmPassword):
                # User authentication creation
                user = User.objects.create_user(first_name=businessName, username=userName, email=email, password=password)
                user.save()

                # Other information saved to database
                userInfo = models.BusinessInfo(user=user, streetAddress=streetAddress, city=city, country=country, suburb=suburb, postalCode=postalCode, phoneNumber=contactNumber)
                userInfo.save()

                return HttpResponseRedirect(reverse('flickboutique:businessSignupSuccess'))

    context = {
        'form' : form,
    }

    return render(request, 'flickboutique/businessSignup.html', context)


def customerLogin(request):
    form = forms.CustomerLoginForm()

    # When the form is submitted, validate the form
    if request.method == 'POST':

        submittedForm = forms.CustomerLoginForm(request.POST) # User data submitted is stored in form

        if submittedForm.is_valid(): # Server-side validation
            userName = submittedForm.cleaned_data['userName']
            password = submittedForm.cleaned_data['password']

            user = authenticate(username=userName, password=password)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('flickboutique:customerHome'))
            else:
                return render(request, 'flickboutique/customerLogin.html', {
                    'form' : form,
                    'error' : "User does not exist.",
                })
    
    return render(request, 'flickboutique/customerLogin.html', {
        'form' : form,
    })


def businessLogin(request):

    form = forms.BusinessLoginForm()

    # When the form is submitted, validate the form
    if request.method == 'POST':

        submittedForm = forms.BusinessLoginForm(request.POST) # User data submitted is stored in form

        if submittedForm.is_valid(): # Server-side validation
            userName = submittedForm.cleaned_data['userName']
            password = submittedForm.cleaned_data['password']

            user = authenticate(username=userName, password=password)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('flickboutique:businessHome'))
            else:
                return render(request, 'flickboutique/businessLogin.html', {
                    'form' : form,
                    'error' : "User does not exist.",
                })

    context = {
        'form' : form,
    }
    return render(request, 'flickboutique/businessLogin.html', context)


def customerHome(request):

    # Return to landing page if user is not logged in
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('flickboutique:index'))

    products = models.Product.objects.order_by('-productRating').all()

    context = {
        'products' : products,
    }

    return render(request, 'flickboutique/customerHome.html', context)


def businessHome(request):

    # Return to landing page if user is not logged in
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('flickboutique:index'))

    products = models.Product.objects.filter(soldBy=request.user)

    context = {
        'products' : products,
        'userinfo': models.BusinessInfo.objects.get(user=User.objects.get(username=request.user.username)),
    }

    return render(request, 'flickboutique/businessHome.html', context)


def productPage(request, productURL):

    context = {
        'product': models.Product.objects.get(productURL=productURL)
    }

    # Return to landing page if user is not logged in
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('flickboutique:index'), context)

    return render(request, 'flickboutique/productPage.html', context)


def businessView(request, username):

    # Return to landing page if user is not logged in
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('flickboutique:index'))

    businessUser = models.User.objects.get(username=username)
    products = models.Product.objects.filter(soldBy=businessUser)

    context = {
        'products' : products,
        'userinfo': models.BusinessInfo.objects.get(user=businessUser),
    }

    return render(request, 'flickboutique/businessView.html', context)


def registerProduct(request):

    # Return to landing page if user is not logged in
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('flickboutique:index'))

    if request.method == 'POST':

        submittedForm = forms.ProductRegistrationForm(request.POST, request.FILES)

        print(request.FILES)

        if submittedForm.is_valid():
            productName = submittedForm.cleaned_data['productName']
            productDepartment = submittedForm.cleaned_data['productDepartment']
            productPrice = submittedForm.cleaned_data['productPrice']
            productInformation = submittedForm.cleaned_data['productInformation']
            productImage = request.FILES['productImage']
            productURL = productName.replace(' ', '-')
            newProduct = models.Product.objects.create(productName=productName, productDepartment=models.ProductDepartment.objects.get(id=productDepartment), productPrice=productPrice, productImage=productImage, productInformation=productInformation, productURL=productURL)
            newProduct.soldBy.add(request.user)
            newProduct.save()

            return HttpResponseRedirect(reverse("flickboutique:businessHome"))
        else:
            context = {
                'form' : forms.ProductRegistrationForm(),
                'error' : 'Something went wrong.'
            }
            return render(request, 'flickboutique/registerProduct.html', context)
        


    context = {
        'form' : forms.ProductRegistrationForm()
    }

    return render(request, 'flickboutique/registerProduct.html', context)


def previewSiteChanges(request):

    # Return to landing page if user is not logged in
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('flickboutique:index'))

    if request.method == 'GET':
        accentColor = request.GET.get('accentColor')
        backgroundColor = request.GET.get('backgroundColor')
        textColor = request.GET.get('textColor')
        secondaryTextColor = request.GET.get('secondaryTextColor')
        productCardColor = request.GET.get('productCardColor')
        productCardGlowColor1 = request.GET.get('productCardGlowColor1')
        productCardGlowColor2 = request.GET.get('productCardGlowColor2')


        context = {
            'accentColor': accentColor,
            'backgroundColor': backgroundColor,
            'textColor': textColor,
            'secondaryTextColor': secondaryTextColor,
            'productCardColor': productCardColor,
            'productCardGlowColor1': productCardGlowColor1,
            'productCardGlowColor2': productCardGlowColor2,
            'userinfo': models.BusinessInfo.objects.get(user=User.objects.get(username=request.user.username)),
        }

        return render(request, 'flickboutique/previewSiteChanges.html', context)

    if request.method == 'POST':

        accentColor = request.POST.get('accentColor')
        backgroundColor = request.POST.get('backgroundColor')
        textColor = request.POST.get('textColor')
        secondaryTextColor = request.POST.get('secondaryTextColor')
        productCardColor = request.POST.get('productCardColor')
        productCardGlowColor1 = request.POST.get('productCardGlowColor1')
        productCardGlowColor2 = request.POST.get('productCardGlowColor2')

        user = models.BusinessInfo.objects.get(user=User.objects.get(username=request.user.username))

        if not user.colorScheme:
            scheme = models.ColorScheme.objects.create(schemeName=request.user.username, accentColor=accentColor, backgroundColor=backgroundColor, textColor=textColor, secondaryTextColor=secondaryTextColor, productCardColor=productCardColor, productCardGlowColor1=productCardGlowColor1, productCardGlowColor2=productCardGlowColor2)
            scheme.save()
            user.colorScheme = scheme
            user.save()
        else:
            user.colorScheme.accentColor = accentColor
            user.colorScheme.backgroundColor = backgroundColor
            user.colorScheme.textColor = textColor
            user.colorScheme.secondaryTextColor = secondaryTextColor
            user.colorScheme.productCardColor = productCardColor
            user.colorScheme.productCardGlowColor1 = productCardGlowColor1
            user.colorScheme.productCardGlowColor2 = productCardGlowColor2
            user.colorScheme.save()
            user.save()
            

        return HttpResponseRedirect(reverse("flickboutique:businessHome"))


    return render(request, 'flickboutique/previewSiteChanges.html')


def manageSite(request):

    # Return to landing page if user is not logged in
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('flickboutique:index'))

    if request.method == 'POST':
        logo = request.FILES['logo']
        userinfo = models.BusinessInfo.objects.get(user=User.objects.get(username=request.user.username))
        userinfo.colorScheme.logo = logo
        userinfo.colorScheme.save()

        return HttpResponseRedirect(reverse('flickboutique:businessHome'))


    
    context = {
        'userinfo': models.BusinessInfo.objects.get(user=User.objects.get(username=request.user.username)),
    }
   
    return render(request, 'flickboutique/manageSite.html', context)


def customerLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('flickboutique:index'))


def businessLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('flickboutique:index'))


def deleteProduct(request):
    if request.method == 'POST':
        deletingProduct = request.POST.get('productURL')
        models.Product.objects.get(productURL=deletingProduct).soldBy.remove(request.user)
        return HttpResponseRedirect(reverse('flickboutique:businessHome'))


def rateProduct(request):
    if request.method == 'POST':
        productName = request.POST.get('productName')
        productRating = int(request.POST.get('productRating'))
        product = models.Product.objects.get(productName=productName)

        # Fetch model values
        if product.productRatingsSum:
            sumRatings = product.productRatingsSum
        else:
            sumRatings = 0
            
        totalRatings = product.productTotalRatings

        # Update model values
        sumRatings += productRating
        totalRatings += 1

        product.productRatingsSum = sumRatings
        newRating = sumRatings / totalRatings
        product.productRating = newRating
        product.productTotalRatings = totalRatings
        product.productRaters.add(request.user)
        product.save()


        return HttpResponseRedirect(reverse('flickboutique:productPage', kwargs={'productURL': product.productURL}))
    

def commentProduct(request):
    if request.method == 'POST':
        commenter = request.POST.get('commenter')
        commentBody = request.POST.get('commentBody')
        product = request.POST.get('product')

        userCommenter = models.User.objects.get(username=commenter)
        productCommented = models.Product.objects.get(productURL=product)
        newComment = models.ProductComment.objects.create(commenter=userCommenter, commentBody=commentBody)
        newComment.save()

        productCommented.productComments.add(newComment)
        productCommented.save()

        return HttpResponseRedirect(reverse('flickboutique:productPage', kwargs={'productURL': productCommented.productURL}))


def replyProductComment(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        replier = request.POST.get('replier')
        replyBody = request.POST.get('replyBody')
        product = request.POST.get('product')

        userReplier = models.User.objects.get(username=replier)
        productCommented = models.Product.objects.get(productURL=product)
        newReply = models.ProductCommentReply.objects.create(replier=userReplier, replyBody=replyBody)
        newReply.save()
        commentModel = models.ProductComment.objects.get(id=comment)
        commentModel.replies.add(newReply)
        commentModel.save()

        return HttpResponseRedirect(reverse('flickboutique:productPage', kwargs={'productURL': productCommented.productURL}))


def businessProfilePage(request, username):

    business = models.User.objects.get(username=username)
    businessInfo = models.BusinessInfo.objects.get(user=business)

    context = {
        'business': business,
        'businessInfo': businessInfo,
    }

    return render(request, 'flickboutique/businessProfilePage.html', context)