from django.contrib import admin
from django.urls import path, include

from django.shortcuts import redirect

urlpatterns = [
    # мой вариант
    # path('admin/', admin.site.urls),
    # path('', include('meals.urls'))

    # вариант чат гпт
    path('', lambda request: redirect('meals/')),
    path('admin/', admin.site.urls),
    path('meals/', include('meals.urls')),
]
