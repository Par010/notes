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

class ChecklistSerializer(ModelSerializer):
    class Meta:
        model = Checkcontent
        fields = [
            'checkbox',
            'check_text'
        ]

class NoteSerializer(ModelSerializer):
    # user_id = SerializerMethodField()
    alert = SerializerMethodField()  # boolean field to indicate reminder status
    url = note_detail_url
    tags = MultipleChoiceField(choices=TAGS, allow_blank=True)
    checklists = ChecklistSerializer(many=True)


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
            'last_modified',
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

    def update(self, instance, validated_data):
        # note = Note.objects.create(**validated_data)
        checklists_data = validated_data.pop('checklists')
        checklist = instance.checklists
        instance.title = validated_data.get('title', instance.title)
        instance.content_plain = validated_data.get('content_plain', instance.content_plain)
        instance.reminder_date = validated_data.get('reminder_date', instance.reminder_date)
        instance.tags = validated_data.get('tags', instance.tags)
        # note = Note.objects.create(**validated_data)
        instance.save()
        # instance.checkbox = validated_data.get('checkbox', instance.checkbox)
        # instance.check_text = validated_data.get('check_text', instance.check_text)
        for checklist_data in checklists_data:
            checklist.checkbox = checklist_data.get(
                'checkbox',
                checklist.checkbox
            )
            checklist.check_text = checklist_data.get(
                'check_text',
                checklist.check_text
            )
            checklist.save()
        # for checklist_data in checklists_data:
        #     checklist_data, created = Checkcontent.objects.get_or_create(checkbox=checklist_data['checkbox'])
        #     checklist_data, created = Checkcontent.objects.get_or_create(check_text=checklist_data['check_text'])
        #     note.checklists.add(checklist_data)
        return instance
