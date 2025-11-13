from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('catalog/', views.catalog, name='catalog'),
    path('catalog/notebooks/', views.notebooks, name='notebooks'),
    path('catalog/phones/', views.phones, name='phones'),
    path('catalog/phones/apple', views.apple, name='apple'),
    path('catalog/phones/apple/iphone16', views.iphone16, name='iphone16'),
    path('catalog/phones/apple/iphone17', views.iphone17, name='iphone17'),
    path('confidentiality', views.confidentiality, name='confidentiality'),
]