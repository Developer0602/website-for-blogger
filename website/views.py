from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import blog


def index(request):
    queryset = blog.objects.filter(status=1).order_by('-created_on')
    context = {'titles': queryset}
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def trash(request):
    return render(request, 'trash.html')


def post_detail(request, slug):
    post = get_object_or_404(blog, slug=slug)
    return render(request, 'post_detail.html', {'check': post})
