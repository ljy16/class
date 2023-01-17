from django.shortcuts import render


def index(request):
    
    # Res -> HTML Render
    # render(1. reqeust | 2. html 이름 | 3. 넘길 데이터)
    return render(request, 'review/index.html')

def hello(request):
    return render(request, 'review/hello.html')
