from django.shortcuts import render, redirect, get_object_or_404
from .models import Author


def author_list(request):
    authors = Author.objects.all()
    ctx = {'authors': authors}
    return render(request, 'authors/authors-list.html', ctx)

def author_create(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        dob = request.POST.get('dob')
        phone = request.POST.get('phone')
        image = request.FILES.get('image')
        if first_name and last_name and dob and phone and image:
            Author.objects.create(
                first_name  = first_name,
                last_name = last_name,
                dob = dob,
                phone = phone,
                image = image,
            )
            return redirect('authors:list')
    return render(request,'authors/author-create.html')

def author_delete(request, pk):
    author = get_object_or_404(Author, pk=pk)
    author.delete()
    return redirect('authors:list')