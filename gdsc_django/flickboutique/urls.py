from django.urls import path
from . import views

app_name = 'flickboutique'

urlpatterns = [
    path("", views.index, name="index")
]