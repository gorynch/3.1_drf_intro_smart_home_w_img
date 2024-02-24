from django.urls import path

from measurement import views

# зарегистрируйте необходимые маршруты
urlpatterns = [
    path('sensors/', views.SensorsView.as_view()),
    path('sensors/<int:pk>/', views.SensorIdView.as_view()),
    path('measurements/', views.MeasurmentView.as_view())
]