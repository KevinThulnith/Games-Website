from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('game/<str:n>/', views.number, name='nmbr'),
    path('profile/', views.loadProfile, name='profile'),
    path('slides/', views.slides, name='slides'),
]
