from django.urls import path
from .import views

app_name = 'data'

urlpatterns = [
    # full url -> data/
    path('', views.index, name='index'),

    # data/hello/<name>/ -> Variable Routing
    path('hello/<name>/', views.hello, name='hello'),
    # hello/neo/ -> 안녕 neo
    # hello/andy -> 안녕 andy


    # full url -> data/input/
    path('user_input/', views.user_input, name='user_input'),
    
    # data/user_output
    path('user_output/', views.user_output, name='user_output'),

]
