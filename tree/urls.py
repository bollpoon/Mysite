from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('loginOK/', views.loginOK, name='loginOK'),
    path('circle/',views.circle, name = 'circle'),
    path('add/',views.add, name = 'add'),
    path('message/',views.message, name = 'message'),
    path('box/',views.box, name = 'box'),
    path('_self/',views._self, name = '_self')
]
