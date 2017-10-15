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

from note.models import Note, Checkcontent, Othertags
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


class OthertagsSerializer(ModelSerializer):
    class Meta:
        model = Othertags
        fields = [
            'tag'
        ]


class NoteSerializer(ModelSerializer):
    alert = SerializerMethodField()  # boolean field to indicate reminder status
    url = note_detail_url
    tags = MultipleChoiceField(choices=TAGS, allow_blank=True)
    checklists = ChecklistSerializer(many=True)     #using nested serializer for checklists
    user_tags = OthertagsSerializer(many=True)

    class Meta:
        model = Note
        fields = [
            # 'user',
            'url',
            'alert',
            'title',
            'content_plain',
            'checklists',
            'create_date',
            'last_modified',
            'reminder_date',
            'tags',
            'user_tags',
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
        user_tags_data = validated_data.pop('user_tags')
        note = Note.objects.create(**validated_data)
        for checklist_data in checklists_data:
            Checkcontent.objects.create(note=note, **checklist_data)    #create checklist objects against a note
        for user_tag_data in user_tags_data:
            Othertags.objects.create(note=note, **user_tag_data)
        return note

    def update(self, instance, validated_data):
        checklists_data = validated_data.pop('checklists')
        checklists = (instance.checklists).all()   #get all checklists objects
        checklists = list(checklists)      #get the objects in list form
        user_tags_data = validated_data.pop('user_tags')
        user_tags = (instance.user_tags).all()
        user_tags = list(user_tags)
        instance.title = validated_data.get('title', instance.title)
        instance.content_plain = validated_data.get('content_plain', instance.content_plain)
        instance.reminder_date = validated_data.get('reminder_date', instance.reminder_date)
        instance.tags = validated_data.get('tags', instance.tags)
        instance.save()

        for checklist_data in checklists_data:
            checklist = checklists.pop(0)       #one checklists object chosen at a time by pop
            checklist.checkbox = checklist_data.get('checkbox', checklist.checkbox)  #get checkbox for that object
            checklist.check_text = checklist_data.get('check_text', checklist.check_text)    #get check_text for that object
            checklist.save()    #save the object

        for user_tag_data in user_tags_data:
            user_tag = user_tags.pop(0)
            user_tag.tag = user_tag_data.get('tag', user_tag.tag)
            user_tag.save()

        return instance
