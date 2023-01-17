from django.db import models

class Article(models.Model):
    # id는 자동으로 만들어짐
    
    # CharField(길이제한 숫자) -> 짧은 str
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=100)
    # TextField -> 긴 str
    content = models.TextField()

# 1. models.py작성
# 2. python manage.py makemigrations <app_name>
# 3. python manage.py migrate <app_name>