from django.urls import path
from . import views # all functions in views

urlpatterns = [
    path('', views.home, name = 'dram-home'),
    path('about/', views.about, name = 'dram-about'),
    
]
