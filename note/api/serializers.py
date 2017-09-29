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
TAGS = (('work', 'Work'),#wo
        ('school-college', 'School/College'),#sco
          ('home', 'Home'),
          ('hobby', 'Hobby'),
          ('others', 'Others'))

note_detail_url = HyperlinkedIdentityField(
    view_name = 'note-detail',      #url to detail view
    read_only = True
)
class NoteSerializer(ModelSerializer):
    # user_id = SerializerMethodField()
    alert = SerializerMethodField()  # boolean field to indicate reminder status
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
        ]

        extra_kwargs = {
        'create_date' : {'read_only': True}   #making create_date read_only
        }

    def get_alert(self, obj):
        local_tz = pytz.timezone('Asia/Kolkata')
        now = datetime.datetime.utcnow().replace(tzinfo=utc).astimezone(local_tz)  #getting datetime with timezone info
        reminder = str(obj.reminder_date)
        reminder_sameformat = dateparse.parse_datetime(reminder)  #converting ISO8601 format to default datetime format
        # print(reminder_sameformat)
        # print(now)
        # type(reminder_sameformat)
        # type(now)
        if obj.reminder_date == None:
            return False
        elif reminder_sameformat.strftime("%Y-%m-%d %H:%M:%S")  <= now.strftime("%Y-%m-%d %H:%M:%S") :  #check if reminder time is behind current time, if yes set alert True
            return True
        else:
            return False
