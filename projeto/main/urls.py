from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('publicacoes/', views.publicacoes, name='publicacoes'),
    path('utilizadores/', views.utilizadores, name='utilizadores'),
]
