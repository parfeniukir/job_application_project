from django.contrib import messages  # Для відображення повідомлень користувачу
from django.shortcuts import render  # Для рендерингу шаблонів
from django.core.mail import EmailMessage  # Для надсилання email

from .forms import ApplicationForm  # Імпорт форми заявки
from .models import Form  # Імпорт моделі заявки

# Файл views.py містить функції-представлення (views) для обробки HTTP-запитів.
# Тут ми зазвичай пишемо логіку для отримання, обробки та повернення даних у відповідь на запити користувача.
# Представлення відповідають за взаємодію між моделями, формами та шаблонами.


def index(request):
    """
    Головна сторінка, яка обробляє форму заявки.
    Якщо метод POST — обробляємо дані форми, зберігаємо їх у базі та надсилаємо email.
    """
    if request.method == "POST":
        form = ApplicationForm(
            request.POST
        )  # Створюємо екземпляр форми з даними користувача
        if form.is_valid():  # Перевіряємо валідність форми
            # Отримуємо дані з форми
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            email = form.cleaned_data.get("email")
            date = form.cleaned_data.get("date")
            occupation = form.cleaned_data.get("occupation")

            # Зберігаємо дані у базі даних
            Form.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                date=date,
                occupation=occupation,
            )

            # Формуємо текст повідомлення для email
            message_body = (
                "New job application recieved\n\n"
                f"Name: {first_name} {last_name}\n"
                f"Date: {date}\n"
                f"Occupation: {occupation}\n"
                f"Thanl you."
            )
            # Створюємо email-повідомлення
            email_message = EmailMessage(
                subject="New Job Application",
                body=message_body,
                to=[
                    email,
                    "1998ivankaa@gmail.com",
                ],  # Надсилаємо заявнику та адміністратору
            )
            email_message.send()  # Відправляємо email

            # Відображаємо повідомлення про успішну відправку заявки
            messages.success(
                request=request,
                message=f"Application submitted successfuly for {first_name}",
            )

            # Виводимо дані у консоль для дебагу
            # print(f"{first_name}, {last_name}, {email}, {date}, {occupation}")

    # Рендеримо головну сторінку (GET-запит або після обробки POST)
    return render(request=request, template_name="index.html")


def about(request):
    """
    Сторінка 'Про нас'.
    """
    return render(request=request, template_name="about.html")


# TODO: add contacts
# def contacts(request):
#     pass
