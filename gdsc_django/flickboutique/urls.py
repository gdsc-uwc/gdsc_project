from django.urls import path
from . import views

app_name = 'flickboutique'

urlpatterns = [
    path("", views.index, name="index"),
    path("customer-signup", views.customerSignup, name="customerSignup"),
    path("business-signup", views.businessSignup, name="businessSignup"),
]