from django.urls import path
from . import views

"""
    url verme şekli
    app_name = "template_app"

"""
app_name = "template_app"

urlpatterns = [
    path('', views.index, name="index"),
    path('weather/', views.weather_view, name="weatherview")
]