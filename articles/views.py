from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from articles.forms import ArticleForm
from articles.models import Article


def articles(request):
    articles = Article.objects.order_by('-date')
    return render(request, 'articles/article.html', {'articles': articles})

def detail(request, article_id):
    articles = get_object_or_404(Article, pk=article_id)
    return render(request, 'articles/details.html', {'articles': articles})

    
@login_required(login_url="login")
def create_article(request):
    form = ArticleForm()    
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles')
    context = {'form': form}
    return render(request, 'articles/form.html', context)