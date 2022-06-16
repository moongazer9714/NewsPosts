from django.urls import path
from .views import PostDetail, PostList


urlpatterns = [
    # path('', views.getRoutes),
    # path('posts/', views.getPosts),
    # path('posts/<str:pk>/', views.getPost),
    path('<str:pk>/', PostDetail.as_view()),
    path('', PostList.as_view()),
]
