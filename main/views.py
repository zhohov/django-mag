from django.shortcuts import render
from .models import Article, Release
from django.views.generic import DetailView


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


class release_detail(DetailView):
    model = Release
    extra_context = {'articles': Article.objects.all()}
    template_name = ('main/release_detai_view.html')
    contex_object_name = 'release'


def released(request):
    releases = Release.objects.all()
    articles = Article.objects.all()
    return render(request, 'main/released.html', {
        'articles': articles,
        'releases': releases
    })
