from django.urls import path
from . import views

# 변수명은 반드시 app_name이어야 함
app_name = 'review'

# URL 구성 맨 앞에 'review/'는 이미 master url에서 검사가 끝났음.
urlpatterns = [
    # 패턴 '(review/)index/'가 요청으로 들어온다면, index함수실행!!
    path('index/', views.index, name='index'),
    # review/hello/
    path('hello/', views.hello, name='hello'),
]

