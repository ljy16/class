from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.


import random

def hello_world(request):
    # 응답으로 html을 렌더링 하겠다.!
    # 장고는 -> 무조건 html 파일은 무조건 templates/ 에서 찾는다.
    return render(request, 'hello_world.html')

def lunch(request):
    menus = ['순대국밥', '보쌈', '치킨', '샐러드', '어머니는 짜장면이 싫다고 하셨어',]
    menu = random.choice(menus)
    context = {
        'menu' : menu
    }
    return render(request, 'lunch.html', context)

def lotto(request):
    numbers = random.sample(range(1,46),6)
    numbers.sort()
    context = {
        'numbers' : numbers, 
        'is_jackpot' : True,
    }
    return render(request, 'lotto.html', context)