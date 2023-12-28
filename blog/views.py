from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Category, Comment, Tag
from .forms import PostForm
from django.db.models import Q
# search with django-watson
from watson import search as watson_search


def home(request):
    posts = Post.objects.all().order_by('-publication_date')
    categories = Category.objects.all()
    tags = Tag.objects.all()
    return render(request, 'home.html', {'posts': posts, 'categories': categories, 'tags': tags})

# get all the posts of a category
def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'blog/category_detail.html', {'category': category})

# filter by tag
def tag_detail(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    return render(request, 'blog/tag_detail.html', {'tag': tag})

# seach a post
def search_post(request):
    post = request.GET.get('post')
    category = request.GET.get('category')
    q_objects = Q()

    if category:
        q_objects &= Q(categories__name__icontains=category)

    if post:
        search_fields = ['title', 'content',
                         'tags__name', 'categories__name']
        
        queries = [Q(**{field + '__icontains': post})
                   for field in search_fields]
        
        for query in queries:
            q_objects |= query

    posts = Post.objects.filter(q_objects)
    # Convert Q object to string query
    search_query_str = str(q_objects)
    # Use Watson's search function to perform the search
    #search_results = watson_search.search(
        #search_query_str, models=(Post,))
    context = {
        'posts': posts,
        # print search_results and compare to posts
        # 'search_results': search_results,
        'category': category,
        'post': post,
       
    }
    return render(request, 'blog/search_post.html', context)
    

# def filter_by_category(request, pk):
#     category = get_object_or_404(Category, pk=pk)
#     posts = Post.objects.filter(category=category)
#     categories = Category.objects.all()
#     tags = Tag.objects.all()

#     return render(request, 'home.html', {'posts': posts, 'categories': categories, 'tags': tags})

# def filter_by_tag(request, pk):
#     tag = get_object_or_404(Tag, pk=pk)
#     posts = Post.objects.filter(tags=tag)
#     categories = Category.objects.all()
#     tags = Tag.objects.all()

#     return render(request, 'home.html', {'posts': posts, 'categories': categories, 'tags': tags})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form})


@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        # Replace 'home' with the URL name of your home page
        return redirect('home')
    return render(request, 'blog/post_confirm_delete.html', {'post': post})
