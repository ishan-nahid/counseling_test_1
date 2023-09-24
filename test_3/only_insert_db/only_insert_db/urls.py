"""
URL configuration for only_insert_db project.

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
from app_1.views import go_index, welcome, profile, user_login, student_profile, faculty_profile

urlpatterns = [
    path('', welcome),
    path('admin/', admin.site.urls),
    path('sign_up/', go_index),
    path('profile/', profile, name='profile'),
    path('login/', user_login, name='login'),
    path('student_profile/', student_profile, name='student'),
    # path('faculty_profile/', faculty_profile, name='faculty'),
    path('faculty/<str:name>/<str:id>/<str:role>/', faculty_profile, name='faculty'),
]
