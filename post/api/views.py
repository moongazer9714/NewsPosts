from rest_framework.decorators import api_view
from rest_framework.response import Response
from post.models import Post
from.serializers import PostSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from .permissions import IsAuthorOrReadOnly

# @api_view(['GET'])
# def getRoutes(request):
#     routes = [
#         'GET/api',
#         'GET/api/posts',
#         'GET/api/posts/:id'
#     ]
#     return Response(routes)
#
# @api_view(['GET'])
# def getPosts(request):
#     posts = Post.objects.all()
#     serializer = PostSerializer(posts, many=True)
#     return Response(serializer.data)
#
# @api_view(['GET'])
# def getPost(request, pk):
#     post = Post.objects.get(id=pk)
#     serializer = PostSerializer(post, many=False)
#     return Response(serializer.data)


class PostList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

