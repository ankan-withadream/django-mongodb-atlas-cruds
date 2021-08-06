from django.shortcuts import render, redirect
from .models import comments, movies, users

# Create your views here.

def index(request):
    return render(request, 'index.html')

def all_comments(request):
    all_comments = comments.objects.all()
    context = {'all_c':all_comments}
    return render(request, 'comments.html', context)

def add_comment(request):
    adding_c = True
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('phone')
        text = request.POST.get('address')
        new_c = comments(name=name,email=email,text=text)
        new_c.save()
        return redirect('/comments')
    context = {'adding_c':adding_c}
    return render(request, 'add.html', context)

def update_comment(request, name):
    updating_c = True
    old_obj = comments.objects.filter(name=name).first()
    pk = old_obj.name
    if request.method == 'POST':
        old_obj = comments.objects.filter(name=name).first()
        # new_name = request.POST.get('new_name')
        new_email = request.POST.get('new_phone')
        new_text = request.POST.get('new_address')
        # old_obj.name = new_name
        old_obj.email = new_email
        old_obj.text =new_text
        old_obj.save()
        # old_obj = comments.objects.filter(name=name).first()
        # old_obj.delete()
        return redirect('/comments')
    context = {'updating_c':updating_c, 'pk':pk}
    return render(request, 'update.html', context)
        

def delete_comment(request, name):
    old_obj = comments.objects.filter(name=name).first()
    old_obj.delete()
    return redirect('/comments')


def all_movies(request):
    all_movies = movies.objects.all()
    context = {'all_o':all_movies}
    return render(request, 'movies.html', context)


def add_movie(request):
    adding_o = True
    if request.method == 'POST':
        title = request.POST.get('title')
        plot = request.POST.get('plot')
        year = request.POST.get('year')
        rated = request.POST.get('rated')
        new_o = movies(title=title,plot=plot,year=year,rated=rated)
        new_o.save()
        return redirect('/movies')
    context = {'adding_o':adding_o}
    return render(request, 'add.html', context)


def update_movie(request, title):
    updating_o = True
    old_obj = movies.objects.filter(title=title).first()
    pk = old_obj.title
    if request.method == 'POST':
        old_obj = movies.objects.filter(title=title).first()
        # title = request.POST.get('title')
        plot = request.POST.get('plot')
        year = request.POST.get('year')
        rated = request.POST.get('rated')
        # old_obj.title =title
        old_obj.plot = plot
        old_obj.year = year
        old_obj.rated =rated
        old_obj.save()
        # old_obj = movies.objects.filter(title=title).first()
        # old_obj.delete()
        return redirect('/movies')
    context = {'updating_o':updating_o, 'pk':pk}
    return render(request, 'update.html', context)


def delete_movie(request, title):
    old_obj = movies.objects.filter(title=title).first()
    old_obj.delete()
    return redirect('/movies')

def all_users(request):
    all_users = users.objects.all()
    context = {'all_p':all_users}
    return render(request, 'users.html', context)


def add_user(request):
    adding_p = True
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('quantity')
        password = request.POST.get('price')
        new_p = users(name=name, email=email, password=password)
        new_p.save()
        return redirect('/users')
    context = {'adding_p':adding_p}
    return render(request, 'add.html', context)

def update_user(request, name):
    updating_p = True
    old_obj = users.objects.filter(name=name).first()
    pk = old_obj.name
    if request.method == 'POST':
        old_obj = users.objects.filter(name=name).first()
        # new_name = request.POST.get('new_name')
        new_email = request.POST.get('new_quantity')
        new_password = request.POST.get('new_price')
        # old_obj.name = new_name
        old_obj.email = new_email
        old_obj.password = new_password
        old_obj.save()
        # old_obj = users.objects.filter(name=name).first()
        # old_obj.delete()
        return redirect('/users')
    context = {'updating_p':updating_p, 'pk':pk}
    return render(request, 'update.html', context)

def delete_user(request, name):
    old_obj = users.objects.filter(name=name).first()
    old_obj.delete()
    return redirect('/users')