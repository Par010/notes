from django.db import models
from django.conf import settings
from django.utils import timezone
from multiselectfield import MultiSelectField
# Create your models here.
TAGS = (('wo', 'Work'),
          ('hm', 'Home'),
          ('cl', 'School/College'),
          ('hb', 'Hobby'),
          ('ot', 'Others'))


class Note(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content_plain = models.TextField(null=True, blank=True)
    create_date = models.DateField(default=timezone.now().date())
    reminder_date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    last_modified = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True, null=True)
    tags = MultiSelectField(choices=TAGS, blank=True, null=True)
    alert = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user.username)


class Checkcontent(models.Model):
    note = models.ForeignKey(Note, related_name='checklists', default=0, on_delete=models.CASCADE)
    check_text = models.CharField(max_length=60, default=" ")
    checkbox = models.BooleanField(default=False)

    def __str__(self):
        return self.check_text

class Othertags(models.Model):
    note = models.ForeignKey(Note, related_name='user_tags', default=0, on_delete=models.CASCADE)
    tag = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.tag
