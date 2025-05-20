from django.shortcuts import render
from django.shortcuts import redirect

#import forms!!
from .forms import MealForm
#import models!!
from .models import Meals


def list_meals(request):
    meals = Meals.objects.all()
    return render(request, 'meals/list_meals.html')


def create_meal(request):
    if request.method == 'POST':
        form = MealForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('meals')
    else:
        form = MealForm()
    return render(request, 'meals/create_meal.html', {'form': form})

def detail_meal(request):
    return render(request, 'meals/detail_meal.html')


def delete_meal(request):
    return render(request, 'meals/delete_meal.html')


def counting_meal(request):
    return render(request, 'meals/counting_meal.html')