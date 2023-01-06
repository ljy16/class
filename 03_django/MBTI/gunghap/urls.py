from django.urls import path
from .import views

app_name = 'gunghap'

urlpatterns = [
    path('info/', views.info, name='info'),
    path('result/', views.result, name='result'),

]
