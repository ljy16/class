from board.models import Article
# Create 하는 방법

# 1.
article = Article()
article.title = '첫번째 글'
article.content = '내가 처음이다!'
article.author = '이재용'
article.save()

# 2.
article = Article(title='2번글', content='까비', author='lje')
article.save()

# 3.
Article.objects.create(title='3번글', content='아까비', author='홍길동')

## Read / Retrieve (조회)
# 단일조회
article = Article.objects.get(id=1)
# 위에와 같음 -> article = Article.objects.get(pk=1)
article.id
# = article.pk
article.title
article.content
article.author

# 전체조회
articles = Article.objects.all()

#활용
article = Article.object.all()
for article in articles:
    print(article.title)

# Update (수정)
article = Article.objects.get(id=3) # 먼저 수정할 게시글을 고르고,
article.title = '수정한 글'
article.content = '0144!!!'
article.save()

# Delete / Destroy(삭제)
article = Article.objects.get(id=1)
article.delete()