from django.urls import path
from . import views


urlpatterns = [
    path('', views.posts_list, name='posts'),
    path('post/<str:pk>/', views.post_detail, name="post"),
    path('about/', views.about_us, name="about"),

    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),

    path('contact/', views.contactPage, name="contact"),
]
