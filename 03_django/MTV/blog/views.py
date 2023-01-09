from django.shortcuts import render, redirect
from .models import Article

# 글 목록 화면 (Read)
def index(request):
    # 글 목록 조회 
    # => db article 테이블에서 관련된 레코드 전체를 조회

    articles = Article.objects.all() # QuerySet(List)
    context = {
        'articles' : articles,
    }
    return render(request, 'blog/index.html', context)

# 글 상세 화면(Read)
def detail(request, article_pk):
    # db -> articles -> 특정 레코드 조회
    article = Article.objects.get(pk=article_pk)
    context = {
        'article' : article,
    }
    return render(request, 'blog/detail.html', context)

# 글 쓰기 화면 (create)
def new(request):
    return render(request, 'blog/new.html')

# 글 DB에 실제 저장
def create(request):
    # 새로운 article 객체 생성(레코드 추가)
    article = Article()
    article.title = request.POST['title']
    article.content = request.POST['content']
    # save할때 id확정됨.
    article.save()

    # detail로 redirect하자!
    return redirect('blog:detail', article.pk)

# 글 수정 화면
def edit(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context={
        'article':article,
    }
    return render(request, 'blog/edit.html', context)

# 글 DB에 실제 수정
def update(request, article_pk):
    # 기존의 article 객체 조회(레코드 검색)
    article = Article.objects.get(pk=article_pk)
    article.title = request.POST['title']
    article.content = request.POST['content']
    # save할때 id확정됨.
    article.save()

    # detail로 redirect하자!
    return redirect('blog:detail', article.pk)


# 글 삭제 (dalete)
def delete(request, article_pk):
    if request.method == 'POST':
        # 1. 특정 게시글 지운다.(고른다.)
        article = Article.objects.get(pk=article_pk)
        # 2. 지운다.
        article.delete()
    # 삭제했으니 목록으로 바로 보여줌
    return redirect('blog:index')