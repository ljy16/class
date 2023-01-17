from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    # articles/create/ (master_app에 path에서 접두사를 articles로 설정함.)
    path('create/', views.create_article, name='create_article'),

    # articles/
    path('', views.article_index, name='article_index'),

    # articles/1
    path('<int:article_pk>/', views.article_detail, name='article_detail'),

    # articles/1/comments/create/
    path('<int:article_pk>/comments/create/', views.create_comment, name='create_comment'),

    # articles/1/comments/2/delete/ -> 1번 게시글에 달려있는 2 번 댓글을 삭제하겠다.!
    path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.delete_comment, name='delete_comment'),

    # articles/1/update/
    path('<int:article_pk>/update/', views.update_article, name='update_article'),

    # articles/1/delete/
    path('<int:article_pk>/delete/', views.delete_article, name='delete_article'),
]

