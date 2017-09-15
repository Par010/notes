from rest_framework.viewsets import ModelViewSet
from .serializers import NoteSerializer
from note.models import Note
from .permissions import IsOwner
from .pagination import NotePageNumberPagination
from rest_framework.response import Response
# from django.db.models import Q
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
    pagination_class = NotePageNumberPagination
    permission_classes = [IsAuthenticated,IsOwner]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'content_plain', 'tags']
    ordering_fields = ['reminder_date','create_date', 'alert']
    ordering = ['-create_date']
    queryset = Note.objects.all()
    # lookup_field = 'user_id'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = NoteSerializer(queryset, many=True, context={'request': request})
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        return Response(serializer.data)

    def get_queryset(self):
        user = self.request.user.id
        queryset = Note.objects.filter(user=user)
        return queryset
