# admin.py — це файл, який використовується для налаштування адміністративної панелі Django.
# Він дозволяє керувати моделями через зручний інтерфейс адміністратора.
# Завдяки цьому файлу адміністратор може переглядати, редагувати, шукати та фільтрувати дані моделей.

from django.contrib import admin  # Імпортуємо модуль адміністратора Django

from .models import Form  # Імпортуємо модель Form з поточного додатку


# Створюємо клас налаштувань для моделі Form в адмін-панелі
class FormAdmin(admin.ModelAdmin):
    # Вказуємо, які поля будуть відображатися у списку записів
    list_display = ("first_name", "last_name", "email", "date", "occupation")
    # Додаємо можливість пошуку по зазначених полях
    search_fields = ("first_name", "last_name", "email", "occupation")
    # Додаємо фільтри для полів "date" та "occupation"
    list_filter = ("date", "occupation")
    # Встановлюємо порядок сортування записів (за спаданням дати)
    ordering = ("-date",)
    # Робимо поля "email" та "occupation" лише для читання (неможливо змінити через адмінку)
    readonly_fields = ("email", "occupation")


# Реєструємо модель Form та її налаштування в адміністративній панелі
admin.site.register(Form, FormAdmin)
