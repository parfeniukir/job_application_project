"""
URL configuration for src project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# Список маршрутів (URL patterns) для проєкту Django.
# Тут визначаються всі шляхи, які обробляються додатком.
# Це потрібно для того, щоб сервер знав, які функції чи класи викликати при зверненні до певних URL.

urlpatterns = [
    # Адмін-панель Django. Дозволяє керувати даними через веб-інтерфейс.
    path('admin/', admin.site.urls),

    # Головна сторінка та всі маршрути додатку job_application.
    # include дозволяє підключити маршрути з іншого файлу (job_application/urls.py).
    # Це робить структуру проєкту більш організованою та зручною для підтримки.
    path("", include("job_application.urls")),
]
