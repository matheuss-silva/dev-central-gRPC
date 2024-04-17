from django.contrib import admin
from django.urls import path
from notificacoes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('send-notification/', views.send_notification, name='send_notification'),
]

