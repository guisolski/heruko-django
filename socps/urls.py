"""socps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

import mysite.views

urlpatterns = [
	path("", mysite.views.index, name="index"),
	path("page2/", mysite.views.page2, name="page2"),
	path("page3/", mysite.views.page3, name="page3"),
    path("page4/", mysite.views.page4, name="page4"),
    path("page5/", mysite.views.page5, name="page5"),
    path('admin/', admin.site.urls),
]

