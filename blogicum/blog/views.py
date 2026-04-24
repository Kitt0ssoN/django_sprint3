from django.utils import timezone
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Category, Post


def get_published_posts():
    return Post.objects.select_related(
        'category',
        'location',
        'author'
    ).only(
        'id',
        'title',
        'pub_date',
        'text',
        'category__slug',
        'category__title',
        'location__is_published',
        'location__name',
        'author__username'
    ).filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    )


def index(request: HttpRequest) -> HttpResponse:
    post_list = get_published_posts()[:5]

    context = {'post_list': post_list}

    return render(request, 'blog/index.html', context)


def post_detail(request: HttpRequest, id: int) -> HttpResponse:
    post = get_object_or_404(get_published_posts(), pk=id)

    context = {'post': post}

    return render(request, 'blog/detail.html', context)


def category_posts(request: HttpRequest, category_slug: str) -> HttpResponse:
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )

    post_list = get_published_posts().filter(category=category)

    context = {
        'category': category,
        'post_list': post_list
    }

    return render(request, 'blog/category.html', context)
