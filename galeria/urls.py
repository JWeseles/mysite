from django.urls import path

from .views import index, contato, foto

urlpatterns = [
    path('', index, name='index'),
    path('contato/', contato, name='contato'),
    path('foto/', foto, name='foto'),

]