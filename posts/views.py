from django.shortcuts import render, redirect, get_object_or_404
from authors.models import Author
from catalogs.models import Category
from .models import Post, Comment
from tags.models import Tag
from django.db.models import Count


def home(request):
    posts = Post.objects.all()
    tag = request.GET.get('tag')
    created_at = request.GET.get('created_at')
    updated_at = request.GET.get('updated_at')
    category = request.GET.get('category')
    sort_by = request.GET.get('sort', 'latest')
    if category:
        posts = posts.filter(category__name=category)
    if tag:
        posts = posts.filter(tag__name=tag)
    if created_at and updated_at:
        posts = posts.filter(create_at__range=[created_at, updated_at])
    elif created_at:
        posts = posts.filter(create_at__gte=created_at)
    elif updated_at:
        posts = posts.filter(update_at__lte=updated_at)
    if sort_by == 'latest':
        posts = posts.order_by('-created_at')
    elif sort_by == 'oldest':
        posts = posts.order_by('created_at')
    elif sort_by == 'popular':
        posts = posts.annotate(comment_count=Count('comments')).order_by('-comment_count')
    categories = Category.objects.all()
    tags = Tag.objects.all()
    ctx = {
        'posts': posts,
        'categories': categories,
        'tags': tags,
        'sort_by': sort_by,
    }
    return render(request, 'index_with_side_bar.html', ctx)

def post_list(request):
    posts = Post.objects.all()
    ctx = {'posts': posts}
    return render(request,'posts/posts-list.html', ctx)

def post_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        author = request.POST.get('author')
        image = request.FILES.get('image')
        desc = request.POST.get('desc')
        tag = request.POST.get('tag')
        category = request.POST.get('category')
        if name and author and image and desc and tag and category:
            author = Author.objects.get(id=author)
            category = Category.objects.get(id=category)
            tag = Tag.objects.get(id=tag)
            Post.objects.create(
                name = name,
                author = author,
                image = image,
                desc = desc,
                category = category,
                tag = tag,
            )
            return redirect('posts:list')
    authors = Author.objects.all()
    tags = Tag.objects.all()
    categories = Category.objects.all()
    ctx = {'authors': authors, 'tags': tags, 'categories': categories}
    return render(request,'posts/post-create.html', ctx)

def post_detail(request, pk, year, month, day, slug):
    post = get_object_or_404(
        Post,
        pk=pk,
        slug=slug,
        created_at__year=year,
        created_at__month=month,
        created_at__day=day,
    )
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        if name and email and comment:
            Comment.objects.create(
                post = post,
                name = name,
                email = email,
                comment = comment
            )
            return redirect(request.path_info)
    comments = post.comments.all()
    ctx = {'post': post, 'comments': comments}
    return render(request, 'posts/post-detail.html', ctx)

def contact_list(request):
    return render(request,'contact.html')

def contact_approved(request):
    return render(request,'approved.html')

def about_list(request):
    return render(request,'about.html')

def blog_search(request):
    query = request.GET.get('q')
    posts = Post.objects.all()
    if query:
        posts = posts.filter(name__icontains=query)
    context = {
        'posts': posts,
        'query': query
    }
    return render(request, 'index_with_side_bar.html', context)

