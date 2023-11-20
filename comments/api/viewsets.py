from rest_framework.viewsets import ModelViewSet
from comments.models import Comment
from .serializers import CommentSerializer

class CommentsViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer