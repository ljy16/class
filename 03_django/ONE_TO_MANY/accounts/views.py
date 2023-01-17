from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.views.decorators.http import require_http_methods, require_safe, require_POST

@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user) # 만들자마자 바로 로그인하게 해주는 의미
            return redirect('board:article_index')
    else : 
        form = UserCreationForm()        
    context={'form':form,}
    return render(request, 'accounts/signup.html', context)

@require_http_methods(['GET', 'POST'])
def login(request):
    if request.method == 'POST':
        # 다른 form과 인자가 구성이 다름.
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user) # 팔찌 채워줌
            # None 또는 URL이 들어가있음.
            # next=articels/create/
            next = request.GET.get('next')
            return redirect(next or 'board:article_index')
    else:
        form = AuthenticationForm()
    context={'form':form,}
    return render(request, 'accounts/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect("board:article_index")