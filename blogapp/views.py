from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blogapp/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    return render(request, 'blogapp/post_detail.html', {'post': post, 'comments': comments})

@login_required
def post_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        post = Post.objects.create(title=title, content=content, author=request.user)
        return redirect('post_detail', pk=post.pk)
    return render(request, 'blogapp/post_create.html')
