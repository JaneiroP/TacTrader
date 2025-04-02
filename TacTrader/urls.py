"""
URL configuration for TacTrader project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user_manager.views import get_users, get_user, post_user, update_user, delete_user

urlpatterns = [
    path('api/v1/admin/', admin.site.urls),
    path("api/v1/get/", get_users),
    path("api/v1/get/<int:pk>/", get_user),
    path("api/v1/post/", post_user),
    path("api/v1/patch/<int:pk>/", update_user),
    path("api/v1/delete/<int:pk>/", delete_user),


]
