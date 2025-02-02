from django.shortcuts import render, get_object_or_404, redirect
from .models import Tag


def tag_list(request):
    tags = Tag.objects.all()
    ctx = {'tags': tags}
    return render(request,'tags/tags-list.html', ctx)

def tag_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            Tag.objects.create(
                name = name,
            )
            return redirect('tags:list')
    return render(request,'tags/tag-create.html')

def tag_delete(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    tag.delete()
    return redirect('tags:list')

