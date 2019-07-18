from django.urls import path
from . import views
app_name = 'frontend'

urlpatterns = [
    path('', views.index, name='index'),
    path('etapa2/<int:id>', views.etapa2, name='etapa2'),
    path('etapa3/<int:id>', views.etapa3, name='etapa3'),
]