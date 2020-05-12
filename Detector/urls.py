from django.urls import path

from . import views


urlpatterns = [
    path('', views.Index),
    path('signup/', views.signup),
    path('login/', views.login),
    path('logout/', views.logout),

]
