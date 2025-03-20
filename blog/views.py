from django.shortcuts import get_object_or_404, render, redirect
from .models import Post
from .forms import PostForm

# Create your views here.
def home(request):
    available_posts = Post.objects.all() 
    return render(request,'homepage.html',{"available_posts" : available_posts})

def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request,'post_detail.html',{"post" : post})


def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect("homepage")
    else:
        form = PostForm()
    
    return render(request, "post_create.html", {"form": form})

def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":  
        form = PostForm(request.POST, instance=post)  
        if form.is_valid():
            form.save()
            return redirect("homepage") 
    else:
        form = PostForm(instance=post)  

    return render(request, "post_update.html", {"form": form, "post": post})  

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST": 
        post.delete()
        return redirect("homepage") 

    return render(request, "post_confirm_delete.html", {"post": post})
