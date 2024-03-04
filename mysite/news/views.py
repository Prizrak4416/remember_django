from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import News, Category
from .forms import NewsForm


# def index(request):
#     news = News.objects.all()
#     res = '<h1>Список новостей.</h1>'
#     for new in news:
#         res += f'<div>\n<p>{new.title}</p>\n<p>{new.content}</p>\n</div><hr>'
#     return HttpResponse(res)


def index(request):
    news = News.objects.all()
    return render(request, 'news/index.html',
                  {
                      'news': news,
                      'title': 'Список новостей',
                  })


def test(request):
    return HttpResponse('<h1>Тестовая страница</h1>')


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    return render(request, 'news/category.html',
                  {
                      'news': news,
                      'title': f'Список новостей {category.title}',
                      'category': category
                  })


def view_news(request, news_id):
    # news_item = News.objects.get(pk=news_id)
    news_item = get_object_or_404(News, pk=news_id)
    return render(request, 'news/view_news.html',
                  {
                      'news_item': news_item,
                  })


def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request)
    else:
        form = NewsForm()
    return render(request, 'news/add_news.html', {'form': form})
