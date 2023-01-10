from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    # board
    path('', views.index, name='index'),

    # board/new/
    path('new/', views.new, name='new'),

    # board/create/
    path('create/', views.create, name='create'),

    # board/1/
    path('<int:posting_pk>/', views.detail, name='detail'),

    # board/1/edit(수정)
    path('<int:posting_pk>/edit/', views.edit, name='edit'),

    # board/1/update -> db에 저장하는것
    path('<int:posting_pk>/update/', views.update, name='update'),

    # board/1/delete/
    path('<int:posting_pk>/delete/', views.delete, name='delete'),
]
