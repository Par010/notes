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

class NoteViewSet(ModelViewSet):
    serializer_class = NoteSerializer
    permission_classes = [IsOwner]
    queryset = Note.objects.all()
    # lookup_field = 'user_id'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def list(self, request):
        user = request.user.id
        queryset = Note.objects.filter(user=user)
        serializer = NoteSerializer(queryset, many=True)
        return Response(serializer.data)
