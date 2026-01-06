from django.contrib import messages
from django.shortcuts import render
from django.core.mail import EmailMessage

from .forms import ApplicationForm
from .models import Form


def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            email = form.cleaned_data.get("email")
            date = form.cleaned_data.get("date")
            occupation = form.cleaned_data.get("occupation")

            Form.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                date=date,
                occupation=occupation,
            )

            message_body = (
                "New job application recieved\n\n"
                f"Name: {first_name} {last_name}\n"
                f"Date: {date}\n"
                f"Occupation: {occupation}\n"
                f"Thanl you."
            )
            email_message = EmailMessage(
                subject="New Job Application",
                body=message_body,
                to=[email, "1998ivankaa@gmail.com"],
            )
            email_message.send()

            messages.success(
                request=request,
                message=f"Application submitted successfuly for {first_name}",
            )

            print(f"{first_name}, {last_name}, {email}, {date}, {occupation}")

    return render(request=request, template_name="index.html")


def about(request):
    return render(request=request, template_name="about.html")

# TODO: add contacts
# def contacts(request):
#     pass
