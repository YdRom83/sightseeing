from django.urls import path

from country import views


urlpatterns = [
    path("", views.index, name="index"),
    path("create-country/", views.create_country, name="create-country"),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
]
