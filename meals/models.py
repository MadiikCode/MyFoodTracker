from django.db import models



class Meals(models.Model):
    name = models.CharField(max_length=100)
    calories = models.PositiveIntegerField()
    protein = models.FloatField(null=True, blank=True)
    carbs = models.FloatField(null=True, blank=True)
    fats = models.FloatField(null=True, blank=True)


    def __str__(self):
        return self.name