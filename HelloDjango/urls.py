"""HelloDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from APP import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),    # this for APP
    url(r'^hello/', views.hello),       # this for APP
    url(r'^haha/',views.haha),         # this for APP
    url(r'^App2/',include("APP2.urls")),  # this for APP2
    url(r'^index/',views.index),      # this for APP
    url(r'^home/',views.home),        # this for APP

    # add data
    url(r'^addstudent/',views.add_stu),

    # show data
    url(r'^liststudents/',views.list_stu),


    url(r'^updatestudent/',views.update_stu),

    # delate data
    url(r'^delstudent/',views.del_stu),

    url(r'^APP3/',include('APP3.urls'))




]
