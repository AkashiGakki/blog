from django.urls import path

# 导入包
from . import views

app_name = 'blog'
urlpatterns = [
    # 添加路径
    path('index/', views.index, name='index'),
    path('article/<article_id>', views.article_page, name='article_page'),
    path('edit/<article_id>', views.edit_page, name='edit_page'),
    path('action', views.edit_action, name='edit_action'),
]