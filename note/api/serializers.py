from rest_framework.serializers import (
    CharField,
    ModelSerializer,
    ValidationError,
    SerializerMethodField,
    HyperlinkedIdentityField,
    MultipleChoiceField,
)

from note.models import Note
TAGS = (('work', 'Work'),
        ('school-college', 'School/College'),
          ('home', 'Home'),
          ('hobby', 'Hobby'),
          ('others', 'Others'))

note_detail_url = HyperlinkedIdentityField(
    view_name = 'note-detail',
    read_only = True
)
class NoteSerializer(ModelSerializer):
    # user_id = SerializerMethodField()
    url = note_detail_url
    tags = MultipleChoiceField(choices=TAGS, allow_blank=True)
    class Meta:
        model = Note
        fields = [
            # 'user',
            'url',
            'title',
            'content_plain',
            'create_date',
            'reminder_date',
            'tags',
            # 'user_id'
        ]

    # def get_user_id(self, obj):
    #     return obj.user.id
