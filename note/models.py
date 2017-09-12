from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.
TAGS = (('work', 'Work'),
          ('home', 'Home'),
          ('school-college', 'School/College'),
          ('hobby', 'Hobby'),
          ('others', 'Others'))

class Note(models.Model):
    title = models.CharField(max_length=30)
    content_plain = models.TextField()
    create_date = models.DateField(auto_now_add=True)
    reminder_date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    tags = MultiSelectField(choices=TAGS, blank=True, null=True)
