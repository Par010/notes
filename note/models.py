from django.db import models
from django.conf import settings
from datetime import date
from multiselectfield import MultiSelectField
# Create your models here.
TAGS = (('work', 'Work'),
          ('home', 'Home'),
          ('school-college', 'School/College'),
          ('hobby', 'Hobby'),
          ('others', 'Others'))

class Note(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content_plain = models.TextField()
    create_date = models.DateField(default=date.today())
    reminder_date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    tags = MultiSelectField(choices=TAGS, blank=True, null=True)
    alert = models.BooleanField(default=False)

    # class Meta:
    #     ordering = ['-create_date']

    def __str__(self):
        return str(self.user.username)
