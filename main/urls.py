from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('singin/', views.singIn, name="singin"),
    path('login/', views.loginPage, name="login"),
    path('welcome/', views.welcome, name="welcome"),
    path('logout/', views.logoutPage, name="logout"),
    path('renamepsw/', views.renamePassword, name='rename'),
]
