from django.urls import path
from . import views

urlpatterns = [
    path('generate/pdf/', views.generate_pdf, name='generate_pdf'),
    path('create_user', views.create_users, name='create_users'),
]
