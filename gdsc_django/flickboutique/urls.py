from django.urls import path
from . import views

app_name = 'flickboutique'

urlpatterns = [
    path("", views.index, name="index"),
    path("customer-signup", views.customerSignup, name="customerSignup"),
    path("business-signup", views.businessSignup, name="businessSignup"),
    path("customer-login", views.customerLogin, name="customerLogin"),
    path("business-login", views.businessLogin, name="businessLogin"),
    path("customer-home", views.customerHome, name="customerHome"), # This should later be the index if the user is a customer
    path("business-home", views.businessHome, name="businessHome"), # This should later be the index if the user is a business
    path("manage-site", views.manageSite, name="manageSite"),
    path("product-page", views.productPage, name="productPage"), # Business username should later be added
    path("business-view", views.businessView, name="businessView"), # This should later be changed to the business username
]