from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import Postform

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = Postform(request.POST)
        if form.is_valid():
            form.save()
            form = Postform()
    else:
        form = Postform()

    posts = Post.objects.all()
    return render(request, 'todo/home.html', {'posts' : posts, 'form':form})


def update(request, id):
    data = Post.objects.get(pk=id)
    if request.method=='POST':
        form = Postform(request.POST, instance=data)
        if form.is_valid():
            # data_text = form.cleaned_data['title']
            data.save()
            return HttpResponseRedirect('/')
    form = Postform(instance=data)
    return render(request, 'todo/update.html', {'form':form, 'id':data})


def delete(request, id):
    if request.method == 'POST':
        pi  = Post.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')