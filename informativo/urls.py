from django.urls import path, include
from .views import home, pdf_view,red, inserir

urlpatterns = [
    path('',red),
    path('informativo', home, name='home'),
    path('informativo/<int:key>', pdf_view, name='visualizar'),
    path('informativo/inserir', inserir, name='inserir'),
]
