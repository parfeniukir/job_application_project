from django import forms  # Імпортуємо модуль forms з Django для створення форм®

# Модуль forms дозволяє легко створювати, обробляти та перевіряти HTML-форми у Django-проєктах.


# Оголошуємо клас ApplicationForm, який наслідує від forms.Form
class ApplicationForm(forms.Form):
    # Поле для імені користувача, максимальна довжина — 80 символів
    first_name = forms.CharField(max_length=80)
    # Поле для прізвища користувача, максимальна довжина — 80 символів
    last_name = forms.CharField(max_length=80)
    # Поле для електронної пошти, перевіряє коректність email-адреси
    email = forms.EmailField()
    # Поле для вибору дати, наприклад, дати подачі заявки
    date = forms.DateField()
    # Поле для вказання професії або роду занять, максимальна довжина — 200 символів
    occupation = forms.CharField(max_length=200)
