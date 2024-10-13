from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from articles.forms import ArticleForm
from articles.models import Article
from django.db.models import Q


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


def articles_search(request):
    search_query = request.GET.get("search_query", "")

    if search_query:

        articles = Article.objects.filter(
            Q(title__icontains=search_query) | Q(description__icontains=search_query)
        )
       
    else:
        articles = Article.objects.all()
    context = {
        "search_query": search_query,
        "articles": articles,
    }
    return render(request, "articles/article.html", context)

@login_required(login_url='login')
def update_article(request, pk):
    article = Article.objects.get(id=pk) 
    form = ArticleForm(instance=article)

    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles')

    context = {
        "article": article,
        "form": form,
    }      
    return render(request, "articles/form-update.html", context)  

@login_required(login_url='login')
def delete_article(request, pk):
    article = Article.objects.get(id=pk)

    if request.method == "POST":
        article.delete()
        return redirect('articles')
    context = {
        "article": article
    }
    return render(request, "articles/delete.html", context)