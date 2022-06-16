from django.contrib.auth.models import User
from django.db import models
import uuid
# Create your models here.
from ckeditor.fields import RichTextField
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['title']


class Tag(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ['title']


class Post(models.Model):
    title = models.CharField(max_length=500, null=True, blank=True)
    body = RichTextField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, blank=True, null=True)
    tag = models.ManyToManyField(Tag, blank=True)
    # vote_comment =
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-created_at']

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    content = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.user.username

class Employee(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    job = models.CharField(max_length=500, blank=True, null=True)
    short_bio = RichTextField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
        ordering = ['name']


class About(models.Model):
    title = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'
        ordering = ['title']

class Contact(models.Model):
    name = models.CharField(max_length=500, blank=True, null=True)
    email = models.EmailField(max_length=50, blank=True, null=True)
    subject = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
        ordering = ['name']
