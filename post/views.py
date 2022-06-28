from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.views.generic.edit import DeleteView 
from django.views.generic.edit import CreateView
from .forms import Form_post, Search_post, Form_comment
from .models import Post, Comment
from django.forms.models import model_to_dict





@login_required
def form_post(request):
    if request.method == 'POST':
        form = Form_post(request.POST, files=request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            msj = form.cleaned_data['title']   
            post = Post(title=data ['title'], subtitle=data['subtitle'], text=data['text'],image=data['image'], author=request.user.username)
            post.save()
            return render(request, "home/index.html", {'msj':f'Se creo el post "{msj}"'})
        else:
            return render(request, "post/form_post.html", {'form':form})

    form = Form_post()
    return render(request, "post/form_post.html", {'form':form})


#def AddCommentView(CreateView):
#    model = Comment
#    template_name = 'add_comment.html'
#    fields = '__all__'


@login_required
def form_comment(request, pk: int):
    form = Post.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = Form_comment(request.POST)
        if form.is_valid():
            data = form.cleaned_data
#            msj = form.cleaned_data['form']   
            
#            comment = Comment(post=data['post'], body=data['body'],date=data['date'], author=request.user.username)
#            form.post = data[id_post]
            form.body = data['body']
#            form.date = data['date']
#            form.author=request.user.username
            form.save()
            return render(request, "home/index.html")
#                                                        , {'msj':f'Se creo el comentario "{msj}"'}
        else:
            return render(request, "post/add_comment.html", {'form':form})

    form = Form_comment()
    return render(request, "post/add_comment.html", {'form':form})


def error(request):
    return render (request,'post/error.html')




def detallePost(request, pk: int):
    post = Post.objects.get(pk=pk)
    return render(request, 'post/post_detail.html', context= {'post': post})


@login_required
def update_post(request, pk: int):
    post = Post.objects.get(pk=pk)

    if request.method == 'POST':
        post_form = Form_post(request.POST, request.FILES)
        if post_form.is_valid():
            data = post_form.cleaned_data
            post.title = data['title']
            post.subtitle = data['subtitle']
            post.text = data['text']
            post.image = data['image']
            post.save()

            posts = Post.objects.all()
            context_dict = {
                'posts': posts
            }
            return render(request, "post/blog.html", {'all_posts':posts})

    post_form = Form_post(model_to_dict(post))
    context_dict = {
        'post': post,
        'post_form': post_form,
    }
    return render(
        request=request,
        context=context_dict,
        template_name='post/post_edit.html'
    )


@login_required
def deletePost(request, pk: int):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        post = Post.objects.all()
        context_dict = {
            'post': post
        }
        return render(request=request,
            context=context_dict,
            template_name="home/index.html"
        )
    context_dict = {
        'post': post,
    }
    return render(
        request=request,
        context=context_dict,
        template_name='post/post_confirm_delete.html'
    )
