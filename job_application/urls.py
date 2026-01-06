from django.urls import path  # Імпортуємо функцію path для створення маршрутів

from . import views  # Імпортуємо модуль views з поточного проекту

# Список маршрутів (URL patterns) для додатку
urlpatterns = [
    path("", views.index, name="index"),  # Головна сторінка, викликає функцію index з views
    path("about/", views.about, name="about"),  # Сторінка "About", викликає функцію about з views
    # path("contacts/", views.contacts, name="contact"),  # Сторінка контактів, викликає функцію contacts з views
]
