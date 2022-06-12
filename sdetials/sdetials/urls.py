from django.contrib import admin
from django.urls import path
from enrolment import views

# from sdetials.enrolment.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.showw),
    path('/home', views.show),
    path('done/', views.done),
    path('register/', views.register),
    path('search/', views.search),
]
