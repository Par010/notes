from rest_framework.serializers import (
    CharField,
    ModelSerializer,
    ValidationError,
)

from note.models import Note

class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = [
            # 'user',
            'title',
            'content_plain',
            'create_date',
            'reminder_date',
            'tags',
        ]
