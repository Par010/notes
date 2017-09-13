from rest_framework.serializers import (
    CharField,
    ModelSerializer,
    ValidationError,
    SerializerMethodField,
    HyperlinkedIdentityField,
    MultipleChoiceField,
)
import datetime
import pytz
from django.utils.timezone import utc
from django.utils import dateparse

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
    alert = SerializerMethodField(read_only=True)
    url = note_detail_url
    tags = MultipleChoiceField(choices=TAGS, allow_blank=True)
    class Meta:
        model = Note
        fields = [
            # 'user',
            'url',
            'alert',
            'title',
            'content_plain',
            'create_date',
            'reminder_date',
            'tags',
            # 'user_id'
        ]

        extra_kwargs = {
        'create_date' : {'read_only': True}
        }

    def get_alert(self, obj):
        local_tz = pytz.timezone('Asia/Kolkata')
        now = datetime.datetime.utcnow().replace(tzinfo=utc).astimezone(local_tz)
        reminder = str(obj.reminder_date)
        reminder_sameformat = dateparse.parse_datetime(reminder)
        print(reminder_sameformat)
        print(now)
        # type(reminder_sameformat)
        # type(now)
        if obj.reminder_date == None:
            return False
        elif reminder_sameformat <= now:
            return True
        else:
            return False
    # def get_user_id(self, obj):
    #     return obj.user.id
