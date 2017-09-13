from rest_framework.serializers import (
    CharField,
    ModelSerializer,
    ValidationError,
    SerializerMethodField,
)

from note.models import Note

class NoteSerializer(ModelSerializer):
    # user_id = SerializerMethodField()
    class Meta:
        model = Note
        fields = [
            # 'user',
            'title',
            'content_plain',
            'create_date',
            'reminder_date',
            'tags',
            # 'user_id'
        ]

    # def get_user_id(self, obj):
    #     return obj.user.id
