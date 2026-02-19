from django.urls import path
from . import views

   
urlpatterns = [
    path('register/', views.RegisterUser.as_view()),
    path('', views.AuthLoginUser.as_view(), name='login'),
    path('logout/', views.AuthLogoutUser.as_view())
]