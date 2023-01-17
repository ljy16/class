# hello / urls.py

from django.urls import path
from . import views

urlpatterns = [
    # hello/world -> views.py에서 hello_world 함수를 실행하겠다.
    path('world/', views.hello_world),

    # hello/lunch -> views.py에서 lunch 함수를 실행하겠다.
    path('lunch/', views.lunch),

    path('lotto/', views.lotto),
]