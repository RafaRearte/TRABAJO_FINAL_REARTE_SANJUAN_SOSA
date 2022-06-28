from django.shortcuts import render
from post.models import Post
from user.models import Avatar
from django.db.models import Q


def home(request):
    avatar_ctx = get_avatar_url_ctx(request)
    context_dict = {**avatar_ctx}
    return render(
        request=request,
        context=context_dict,
        template_name="home/index.html"
    )


def about_me(request): 
    return render (request,'home/about_me.html')


def blog(request):
    post = Post.objects.all()
    return render(request, "post/blog.html", {'all_posts':post}) 


def get_avatar_url_ctx(request):
    avatars = Avatar.objects.filter(user=request.user.id)
    if avatars.exists():
        return {'url': avatars[0].image.url}
    return {}


def search(request):
    avatar_ctx = get_avatar_url_ctx(request)
    context_dict = {**avatar_ctx}
    if request.GET['search_param']:
        search_param = request.GET['search_param']
        query = Q(name__contains=search_param)
        query.add(Q(code__contains=search_param), Q.OR)
        posts = Post.objects.filter(query)
        context_dict.update({
            'posts': posts,
            'search_param': search_param,
        })
    return render(
        request=request,
        context=context_dict,
        template_name="home/index.html",
    )
