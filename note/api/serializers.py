from rest_framework.serializers import (
    CharField,
    ModelSerializer,
    ValidationError,
    SerializerMethodField,
    HyperlinkedIdentityField,
    MultipleChoiceField,
    ReadOnlyField,
    BooleanField,
    ModelField,
    PrimaryKeyRelatedField
)
import datetime
import pytz
from django.utils.timezone import utc
from django.utils import dateparse

from note.models import Note, Checkcontent
TAGS = (('wo', 'Work'),#wo
        ('cl', 'School/College'),#sco
          ('hm', 'Home'),
          ('hb', 'Hobby'),
          ('ot', 'Others'))

note_detail_url = HyperlinkedIdentityField(
    view_name = 'note-detail',      #url to detail view
    read_only = True
)

# class ChecktextSerializer(ModelSerializer):
#     class Meta:
#         model = Checktext
#         fields = [
#             'text',
#         ]

    # def create(self, validated_data):
    #     text = validated_data.get('text')
    #     text_data = Checktext.objects.create(text=text)
    #     return text_data


class ChecklistSerializer(ModelSerializer):
    class Meta:
        model = Checkcontent
        fields = [
            'checkbox',
            'check_text'
        ]

    # def create(self, validated_data):
    #     check_text = validated_data.get('check_text')
    #     check_text_data = Checkcontent.objects.create(check_text=check_text)
    #     return check_text_data
    # def create(self, validated_data):
    #     check_text_data = validated_data('check_text')
    #     Checkcontent.objects.create(check_text=check_text_data)

class NoteSerializer(ModelSerializer):
    # user_id = SerializerMethodField()
    alert = SerializerMethodField()  # boolean field to indicate reminder status
    url = note_detail_url
    tags = MultipleChoiceField(choices=TAGS, allow_blank=True)
    checklists = ChecklistSerializer(many=True)
    # checklist = PrimaryKeyRelatedField(many=True, read_only=True)
    # checklist_text = PrimaryKeyRelatedField(many=True, read_only=True)
    # checklist_checkbox = PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Note
        fields = [
            # 'user',
            'url',
            'alert',
            'title',
            'content_plain',
            'checklists',
            # 'checklist_text',
            # 'checklist_checkbox',
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

    # def create(self, validated_data):  #overriding create method to handle foreign key
    #     # note = Note.objects.create(
    #     #     url = validated_data['url'],
    #     #     alert = validated_data['alert'],
    #     #     title = validated_data['title'],
    #     #     content_plain = validated_data['content_plain'],
    #     #     create_date = validated_data['create_date'],
    #     #     reminder_date = validated_data['reminder_date'],
    #     #     tags = validated_data['tags']
    #     # )
    #     note = Note.objects.create(**validated_data)
    #     checklist_text = validated_data.pop('checklist_text', None)
    #     checklist_checkbox = validated_data.pop('checklist_checkbox', None)
    #     checklist_text_create = Checkcontent.objects.create(note=note,**checklist_text)
    #     checklist_checkbox_create = Checkcontent.objects.create(note=note,**checklist_checkbox)
    #     return note
    def create(self, validated_data):
        checklists_data = validated_data.pop('checklists')
        # checklists_text = validated_data.pop('checklists__check_text')
        note = Note.objects.create(**validated_data)
        # Checkcontent.objects.create(note=note, **checklists_data)
        # Note.objects.create(note=note, **checklists_data)

        for checklist_data in checklists_data:
            # Checkcontent.objects.create(note=note, **checklist_data)
            Checkcontent.objects.create(note=note, **checklist_data)
        return note


# for checklist_text in checklists_text:
#     if Checktext.objects.filter(text=checklist_text) == None:
#         Checktext.objects.create(text=checklist_text)
