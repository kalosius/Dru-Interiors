from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.register, name="signup"),
    path("login/", views.signin, name="login"),
    path("furniture/", views.furniture, name="furniture"),
    path("gadgets/", views.gadgets, name="gadgets"),
    path("phones/", views.phones, name="phones"),
    path("product/", views.product, name="product"),
    path("dogs/", views.dogs, name="dogs"),
    path("fashion/", views.fashion, name="fashion"),
]