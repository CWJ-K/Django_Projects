from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView


# Create your views here. function-based view
def post_list(request):
    posts = Post.published.all()
    # Pagination with 3 posts per page
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page', 1)
    try:
        post = paginator.page(page_number)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        post = paginator.page(1)
    return render(request, 'blog/post/list.html', {'posts': post})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )
    return render(request, 'blog/post/detail.html', {'post': post})


# use a class-based view
class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'
