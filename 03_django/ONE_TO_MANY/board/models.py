from django.db import models

class Article(models.Model):
    # id는 자동생성되서 만들필요없음.
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    # id 자동 생성됨.
    content = models.CharField(max_length=200)
    # foreign key 쓰면 필드명에 _id 붙이지 않기
    # migrate하면 알아서 뒤에 _id 붙음.
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

