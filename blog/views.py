from django.shortcuts import render
from blog.models import Postagem


def blog(request):
    postagens = Postagem.objects.all().order_by("-data_criacao")
    return render(request, 'polls/blog.html', {'postagens': postagens})




