from django.urls import path

from .views import view_sensordetail, view_sensors, create_sensor, add_measurement, edit_sensor

urlpatterns = [
    path('view_sensors/', view_sensors.as_view()),
    path('view_sensordetail/', view_sensordetail.as_view()),
    path('create_sensor/<int:id>/<str:name>/<str:description>/', create_sensor.as_view()),
    path('add_measurement/<int:sensor_id>/<int:temperature>/', add_measurement.as_view()),
    path('edit_sensor/<int:pk>/<str:name>/', edit_sensor.as_view())
]
