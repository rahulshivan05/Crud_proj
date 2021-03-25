"""crud_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from enroll.views import add_show, delete_data, update_data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', add_show, name='addandshow'),
    path('delete/<int:id>', delete_data, name='delete_data'),
    path('<int:id>', update_data, name='update_data'),
]
