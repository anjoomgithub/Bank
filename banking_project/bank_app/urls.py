from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('new_page',views.new_page,name='new_page'),
    path('account_application', views.account_application, name='account_application'),
    path('application_success', views.application_success, name='application_success'),
]
