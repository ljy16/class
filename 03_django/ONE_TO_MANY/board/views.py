from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_safe, require_POST
from django.contrib.auth.decorators import login_required

from .models import Article, Comment
from .forms import ArticleForm, CommentForm

@login_required
@require_http_methods(['GET', 'POST'])
def create_article(request):
    
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid(): # 검사에서 통과해야만(True여야) 저장할 수 있음.
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            print(request.user)
            return redirect('board:article_detail', article.pk)
    else:
        form = ArticleForm()
        context = {'form':form,}
        return render(request, 'board/form.html', context)

@require_safe
def article_index(request):
    articles = Article.objects.all()
    context={'articles':articles,}
    return render(request, 'board/index.html', context)


@require_safe
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    form = CommentForm()
    context={
        'article':article,
        'form':form,
    }
    return render(request, 'board/detail.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def update_article(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
        # 글쓴 사람의 user_id와 현재 접속해 있는 id를 비교해서 값이 다를때 접속을 막겠다.
            if request.user != article.user :
                 return redirect('board:article_index')
            article = form.save()
            return redirect('board:article_detail', article.pk)
    else:
            form = ArticleForm(instance=article)
    context={'form':form,}
    return render(request, 'board/form.html', context)

@login_required
@require_POST
def create_comment(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        # 완전 저장시 NOT NULL 에러 뜨니까, 직전에 멈춰달라!
        comment = form.save(commit=False)
        # 나머지는 직접할게여
        comment.user = request.user
        comment.article = article
        comment.save()
    return redirect('board:article_detail', article.pk) # redirect는 request도 context도 필요없음.

@login_required
@require_POST
def delete_comment(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk) # 1개잡을떄는 무조건 getobject404사용
    article = get_object_or_404(Article, pk=article_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('board:article_detail', article.pk )

@login_required
@require_POST
def delete_article(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.user == article.user:
        article.delete()
        return redirect('board:article_index')
    else :
        return redirect('board:article_detail', article.pk)


    # 게시글 삭제하려면 article_pk를 잡아서 삭제하면 될거가툰데
    # 삭제도 글쓴사람의 id와 현재접속해있는 id가 같을때 삭제가 되도록 해야함.


