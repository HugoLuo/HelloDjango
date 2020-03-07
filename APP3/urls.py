from django.conf.urls import url

from APP3 import views

urlpatterns = {
    url(r'^index/',views.index),
    url(r'^getgrade/',views.getgrade),
    url(r'^getstudents/', views.getstudent),

}