from django import forms
from .models import Meals


class MealForm(forms.ModelForm):
    class Meta:
        model = Meals
        fields = [
            'name',
            'calories',
            'protein',
            'carbs',
            'fats',
        ]