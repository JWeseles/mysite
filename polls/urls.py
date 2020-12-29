from django.urls import path

from galeria.views import foto
# from .views import ContatoView, VideosView, EventosView, Dia1View
from .views import ContatoView, VideosView

from .import views


app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index.html'),
    path('<int:pk>/', views.DetailView.as_view(), name='details'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('videos/', VideosView.as_view(), name='videos.html'),
    # path('eventos/', EventosView.as_view(), name='eventos.html'),
    # path('eventos/dia1/', Dia1View.as_view(), name='dia1.html'),
    path('contato/', ContatoView.as_view(), name='contato.html'),
    path('foto/', foto, name='foto'),

]
