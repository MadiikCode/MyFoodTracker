from django.shortcuts import render



def list_meals(request):
    return render(request, 'meals/list_meals.html')


def create_meal(request):
    return render(request, 'meals/create_meal.html')


def detail_meal(request):
    return render(request, 'meals/detail_meal.html')


def delete_meal(request):
    return render(request, 'meals/delete_meal.html')


def counting_meal(request):
    return render(request, 'meals/counting_meal.html')