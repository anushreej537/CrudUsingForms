"""
URL configuration for P1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from A1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('addinfo/',views.addinfo,name='addinfo'),
    path('showinfo/',views.showinfo,name='showinfo'),
    path('updateinfo/<int:id>/',views.updateinfo,name='updateinfo'),
    path('deleteinfo/<int:id>/',views.deleteinfo,name='delete'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('table/',views.table)
]
