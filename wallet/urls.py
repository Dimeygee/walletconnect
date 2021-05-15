from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('wallet/', views.WalletView, name='wallet'),
    path('importwallet/', views.WalletImportView, name='import-wallet'),
    path('success/', views.successView, name='success'),
]
