from django.urls import path
from . import views

urlpatterns = [

    path('', views.blog, name="blog.html")
    # path('post/<int:pk>/', views.detalhe_post, name="detalhe_post"),
]
