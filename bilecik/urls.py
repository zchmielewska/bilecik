from django.contrib import admin
from django.urls import path

from ticket import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.MainView.as_view(), name="main"),
    path('ticket/add', views.AddTicketView.as_view()),
    path('ticket/<ticket_id>', views.TicketDetailView.as_view()),
]
