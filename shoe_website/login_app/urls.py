from django.conf.urls import include
from django.urls import path
from login_app.views import *
urlpatterns = [
    path('', dashboard, name="dashboard"),
    path('collections/<str:slug>', collectionsview, name="collectionsview"),
    path('register/', register, name="register"),
    path('login/', login, name="login"),
    path('cart/', cart, name="cart"),
    path('collections/', collections, name="collections"),
    path("accounts/",include("django.contrib.auth.urls")),
]