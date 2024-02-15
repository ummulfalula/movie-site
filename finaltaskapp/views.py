from django.http import HttpResponse
from django.shortcuts import render, redirect
from.models import Movies
from.forms import MovieForm

# Create your views here.
def index(request):
    obj=Movies.objects.all()
    return render(request,'index.html',{'res':obj})
def detail(request,movie_id):
    movie=Movies.objects.get(id=movie_id)
    return render(request,"detail.html" ,{'movie':movie})


def add_movie(request):
    if request.method=="POST":
        movie_title=request.POST.get('movie_title',)
        poster_img = request.FILES['poster_img']
        desc=request.POST.get('desc',)
        release_date=request.POST.get('release_date',)
        actors = request.POST.get('actors',)
        category = request.POST.get('category',)
        ylink = request.POST.get('ylink',)

        movie=Movies(movie_title=movie_title,poster_img=poster_img,desc=desc,release_date=release_date,actors=actors,category=category,ylink=ylink)
        movie.save()
        return redirect('/')
    return render(request,'add.html')
def update(request,id):
    movie=Movies.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})
def delete(request,id):
    if request.method=='POST':
        movie=Movies.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')