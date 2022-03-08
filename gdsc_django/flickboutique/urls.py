from django.urls import path
from . import views

app_name = 'flickboutique'

urlpatterns = [
    path("", views.index, name="index"),
    path("customer-signup", views.customerSignup, name="customerSignup"),
    path("business-signup", views.businessSignup, name="businessSignup"),
    path("customer-login", views.customerLogin, name="customerLogin"),
    path("business-login", views.businessLogin, name="businessLogin"),
    path("customer-home", views.customerHome, name="customerHome"),
    path("business-home", views.businessHome, name="businessHome"),
    path("manage-site", views.manageSite, name="manageSite"),
    path("product-page", views.productPage, name="productPage"),
]