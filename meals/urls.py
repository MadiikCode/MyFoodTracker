from django.urls import path

from . import views



urlpatterns = [
    path('', views.list_meals, name='meals'),
    path('meals/add/', views.create_meal, name='create_meal'),
    path('detail', views.detail_meal, name='detail'),
    path('meals/<int:meal_id>/delete/', views.delete_meal, name='delete_meal'),
    path('meals/<int:meal_id>/count', views.counting_meal, name='counting_meal'),

 ]
