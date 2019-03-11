from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from . import models

def index(request):
    # 获取所有文章对象，以列表形式传到前端
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})

# 文章页面响应函数
def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/article_page.html', {'article': article})

# 文章编辑页面响应函数
def edit_page(request, article_id):
    if str(article_id) == '0':  # 保险起见，转换成字符串
        return render(request, 'blog/edit_page.html')
    # 否则渲染出修改的文章内容
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/edit_page.html', {'article': article})

# 编辑页面提交响应函数
def edit_action(request):
    # 获取表单传来的值
    title = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')
    article_id = request.POST.get('article_id', '0')
    # 判断
    if str(article_id) == '0':
        # 创建数据
        models.Article.objects.create(title=title, content=content)
        # 返回主页面
        articles = models.Article.objects.all()
        return render(request, 'blog/index.html', {'articles': articles})
    # 否则，修改文章并保存
    article = models.Article.objects.get(pk=article_id)
    article.title = title
    article.content = content
    article.save()
    return render(request, 'blog/article_page.html', {'article': article})