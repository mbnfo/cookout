from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('cook', views.cook, name = 'cook'),
    path('signin', views.signin, name = 'signin'),
    path('<str:f>/', views.food, name='food')
]