from django.shortcuts import render

# Create your views here.
from .models import BlogArticle


def blog_article(request):
    queryset = request.GET.get('tag')
    if queryset:
        blogs = BlogArticle.objects.filter(tag=queryset)
    else:
        blogs = BlogArticle.objects.all()
    context = {}
    context['blogs'] = blogs

    return render(request, 'blog/blog.html', context)
