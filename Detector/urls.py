from django.urls import path

from . import views


urlpatterns = [
    path('', views.index),
    path('index/', views.index),
    path('signup/', views.signup),
    path('login/', views.login),
    path('logout/', views.logout),
    path('uploadImage/', views.XRayImage)
]
