from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q

from post.forms import CommentForm, ContactForm
from post.models import Post, Category, Employee, About, Contact, Comment
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required


def posts_list(request):
    categories = Category.objects.all()
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    posts = Post.objects.filter(Q(title__icontains=q) |
                                Q(body__icontains=q) |
                                Q(author__username__icontains=q) |
                                Q(category__title__icontains=q)
                                )
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    category = request.GET.get('category')
    if category:
        posts = Post.objects.filter(category__title=category)
        paginator = Paginator(posts, 3)
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
    context = {'posts': posts, 'title': 'Islom`s Blog', 'categories': categories}
    return render(request, 'post/index.html', context)


def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    categories = Category.objects.all()
    related_post = Post.objects.all().order_by('-created_at')[:3]
    comments = Comment.objects.filter(post=pk)
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.user = request.user
                form.post = post
                form.save()
                return redirect('post', pk)
        else:
            form = CommentForm()
    else:
        form = CommentForm()
        messages.error(request, 'You have to login You have to login You have to login You have to login You have to login You have to login')
    context = {'post': post, 'related_post': related_post, 'categories': categories, 'comments': comments, 'form': form}
    return render(request, 'post/get_post.html', context)


def about_us(request):
    about = About.objects.all()
    employees = Employee.objects.all()
    context = {'employees': employees, 'about': about, 'title': 'About'}
    return render(request, 'post/about.html', context)


def loginPage(request):
    page = 'login'
    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('posts')
        else:
            messages.error(request, 'Username or password not exist')

    context = {'page': page}
    return render(request, 'post/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('posts')


def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('posts')
        else:
            messages.error(request, 'An error occured during registration')
    context = {'form': form}
    return render(request, 'post/login_register.html', context)


def contactPage(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = Contact(name=request.POST.get('name'), email=request.POST.get('email'),
                              subject=request.POST.get('subject'), message=request.POST.get('message'), )
            contact.save()
            messages.success(request, "Message sent successfully!")
            return redirect('contact')
        else:
            messages.error(request, "Error during sending message!")

    context = {'form': form}
    return render(request, 'post/contact.html', context)
