from . import views
from django.urls import path

urlpatterns = [
    path("",views.index,name="index"),
    path("<int:month>",views.month_challenge_by_number),
    path("<str:month>",views.month_challenge , name="month-challenge")
    
]