from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home-natya'),
    path('about/',views.about, name='about-natya'),
    
]