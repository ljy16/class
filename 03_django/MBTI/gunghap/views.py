from django.shortcuts import render

def info(request):
    return render(request, 'gunghap/info.html')

def result(request):
    return render(request, 'gunghap/result.html')

def combination(request):
    mbti_list = [
            'INFP', 'ENFP', 'INFJ', 'ENFJ',
            'INTJ', 'ENTJ','INTP', 'ENTP',
            'ISFP', 'ESFP','ISTP', 'ESTP',
            'ISFJ', 'ESFJ', 'ISTJ', 'ESTJ'
    ]

    context = {
        'user_mbti' : user_mbti
    }

    render(request, 'gunghap/result.html', context)
   


