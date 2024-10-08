from django.urls import path

from articles import views

urlpatterns = [
    path('', views.articles, name='articles'),
    path('<int:article_id>/', views.detail, name='detail'),
    path('create-article/', views.create_article, name="create-article")
]