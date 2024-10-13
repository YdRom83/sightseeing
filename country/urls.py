from django.urls import path

from country import views


urlpatterns = [
    path("", views.index, name="index"),
    path("create-country/", views.create_country, name="create-country"),
    path("countries/", views.countries, name="countries"),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('update-country/<str:pk>/', views.update_country, name='update-country'),
    path('delete-country/<str:pk>/', views.delete_country, name='delete-country'),
]
