from django.shortcuts import render


def index(request):
    # print(request)
    return render(request=request, template_name="index.html")
