from django.shortcuts import render, redirect
from .models import PostModel
from .forms import PostModelForm

def index(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)# Save the new post
            instance.author = request.user
            instance.save()
            return redirect('blog-index')  # Redirect to the same view after form submission to avoid re-posting
    else:
        form = PostModelForm()

    posts = PostModel.objects.all()  # Queryset to grab all objects in PostModel

    context = {
        'posts': posts,
        'form': form
    }
    return render(request, 'blogmate_app/index.html', context)

def post_detail(request):
    context = {
        
    }
    return render(request, 'blogmate_app/post_detail.html', context)
