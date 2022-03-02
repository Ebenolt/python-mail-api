from django.urls import path
from . import views

urlpatterns = [
    path('', views.start.as_view()), #GET/POST
    path('v1/', views.start.as_view()), #GET/POST
    path('api/', views.start.as_view()), #GET/POST
    path('v1/test/', views.test.as_view()), #GET/POST
    path('v1/send/', views.sendmail.as_view()), #GET/POST
]

