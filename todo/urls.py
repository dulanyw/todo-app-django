from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('topic/create/', views.TopicCreate.as_view(), name='topic_create'),
    path('topic/<int:pk>/edit/', views.TopicEdit.as_view(), name='topic_edit'),
    path('todo/<int:pk>/', views.TodoDetail.as_view(), name='todo_detail'), 
    path('todo/create/', views.TodoCreate.as_view(), name='todo_create'),
    path('todo/<int:pk>/edit/', views.TodoEdit.as_view(), name='todo_edit'),
]