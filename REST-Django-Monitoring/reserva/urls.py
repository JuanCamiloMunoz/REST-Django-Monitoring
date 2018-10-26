from django.urls import path

from . import views

urlpatterns = [
    path('', views.CrearReserva.as_view()),
    path('<int:pk>/', views.ReservaDetail.as_view()),
]
