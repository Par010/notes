from rest_framework.viewsets import ModelViewSet
from .serializers import NoteSerializer

from rest_framework.permissions import(
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

class NoteViewSet(ModelViewSet):
    serializer_class = NoteSerializer
    permission_classes = [IsAdminUser]
    queryset = Note.objects.all()
