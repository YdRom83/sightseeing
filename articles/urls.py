from django.urls import path

from articles import views

urlpatterns = [
    path('', views.articles, name='articles'),
    path('<int:article_id>/', views.detail, name='detail'),
    path('create-article/', views.create_article, name="create-article"),
    path('articles-search/', views.articles_search, name="articles-search"),
    path('update-article/<str:pk>/', views.update_article, name="update-article"),
    path('delete-article/<str:pk>/', views.delete_article, name="delete-article"),
]