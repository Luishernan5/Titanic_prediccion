from django.urls import path
from . import views

urlpatterns = [
    path('', views.prediccion_titanic, name='prediccion_titanic'),
]