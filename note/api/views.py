from rest_framework.viewsets import ModelViewSet
from .serializers import NoteSerializer
from note.models import Note
from .permissions import IsOwner
from rest_framework.response import Response
from rest_framework.permissions import(
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)

class NoteViewSet(ModelViewSet):
    serializer_class = NoteSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'content_plain', 'tags']
    permission_classes = [IsOwner]
    queryset = Note.objects.all()
    # lookup_field = 'user_id'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def list(self, request):
        user = request.user.id
        queryset = Note.objects.filter(user=user)
        serializer = NoteSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
