from django.urls import path

from .views import IndexView, ModelFullView, ModelCleanView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('model_full/', ModelFullView.as_view(), name='model_full'),
    path('model_clean/', ModelCleanView.as_view(), name='model_clean'),
    path('login/', auth_views.LoginView.as_view(
        template_name="home/login.html"
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]


