from django.conf.urls import url
from django.urls import path
from . import views

app_name = "Journal"

urlpatterns = [
    path('Journal', views.landing_page, name='landing_page'),

]
