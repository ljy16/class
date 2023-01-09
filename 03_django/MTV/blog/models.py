from django.db import models

# 1개의 클래스는 1개의 테이블(표)와 매칭됨
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    # 생성시 자동으로 채워지도록 -> DateTimeField만 가능
    created_at = models.DateTimeField(auto_now_add=True)

    # 생성/수정시 자동으로 채워지도록 -> DateTimeField만 가능
    updated_at = models.DateTimeField(auto_now=True)

