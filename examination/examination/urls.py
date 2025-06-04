"""
URL configuration for examination project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("exam.urls")),
    path('',include("students.urls"))

]
#from django.contrib import admin
#from django.urls import path, include  # include for routing to app URLs

#urlpatterns = [
  #  path('admin/', admin.site.urls),  # Admin URLs
  #  path('students/', include('students.urls')),  # Students app URLs
   # path('exam/', include('exam.urls')),  # Exams app URLs
    # Add other paths as needed
#]
