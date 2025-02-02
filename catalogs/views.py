from django.shortcuts import render, redirect, get_object_or_404
from .models import Category


def category_list(request):
    categories = Category.objects.all()
    ctx = {'categories': categories}
    return render(request,'catalogs/catalogs-list.html', ctx)

def category_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            Category.objects.create(
                name = name,
            )
            return redirect('catalogs:list')
    return render(request,'catalogs/catalog-create.html')

def category_delete(request, pk):
    catalog = get_object_or_404(Category, pk=pk)
    catalog.delete()
    return redirect('catalogs:list')