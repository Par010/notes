from rest_framework.serializers import (
    CharField,
    ModelSerializer,
    ValidationError,
    SerializerMethodField,
    MultipleChoiceField,
)

from note.models import Note
TAGS = (('work', 'Work'),
        ('school-college', 'School/College'),
          ('home', 'Home'),
          ('hobby', 'Hobby'),
          ('others', 'Others'))

class NoteSerializer(ModelSerializer):
    # user_id = SerializerMethodField()
    tags = MultipleChoiceField(choices=TAGS, allow_blank=True)
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
