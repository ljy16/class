from django.shortcuts import render, redirect
from .models import Posting

def index(request):
    # 테이블에서 목록 조회
    # db posing에서 레코드 전체 조회
    # 기본 id- > 오름차순
    # postings = Posting.objects.all()

    # id 내림차순 (python)
    # postings = Posting.objects.all()[::-1]

    # id 내림차순 (DB)
    postings = Posting.objects.order_by('-pk')

    context = {
        'postings':postings,
    }
    return render(request, 'board/index.html', context)

# 글 상세 화면(Read)
def detail(request, posting_pk):
    posting = Posting.objects.get(pk=posting_pk)
    context={
        'posting':posting,
    }
    return render(request, 'board/detail.html', context)


# 글 쓰기 화면(new)
def new(request):
    return render(request, 'board/new.html')

# 작성한 데이터 실제 db 저장
def create(request):
    posting = Posting()
    posting.subject = request.POST['subject']
    posting.description = request.POST['description']
    posting.save()

    return redirect('board:detail', posting.pk)

# 수정 화면
def edit(request, posting_pk):
    posting = Posting.objects.get(pk=posting_pk)
    context={
        'posting':posting,
    }
    return render(request, 'board/edit.html', context)
    
# db에 실제 수정
def update(request, posting_pk):
    posting = Posting.objects.get(pk=posting_pk)
    posting.subject = request.POST['subject']
    posting.description = request.POST['description']
    posting.save()

    return redirect('board:detail', posting.pk)


# 삭제
def delete(request, posting_pk):
    if request.method == 'POST':
        posting = Posting.objects.get(pk=posting_pk)
        posting.delete()

    return redirect('board:index')