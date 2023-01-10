from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    # 1. 유효성검사 (validation)
    # 2. html 안에 <input> 태그 만들기 싫다
    # 3. 저장할때 request.POST에서 하나하나 꺼내기 귀찮

    title = forms.CharField(min_length=2, max_length=100)
    

    class Meta:
        model = Article
        fields = ('title', 'content',)

