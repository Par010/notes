from django.db import models
from django.conf import settings
from django.utils import timezone
from multiselectfield import MultiSelectField
# Create your models here.
TAGS = (('work', 'Work'),
          ('home', 'Home'),
          ('school-college', 'School/College'),
          ('hobby', 'Hobby'),
          ('others', 'Others'))

class Checktext(models.Model):
    text = models.CharField(max_length=60)

    def __str__(self):
        return self.text

class Checkcontent(models.Model):
    checkbox = models.BooleanField(default=False)
    text = models.ForeignKey(Checktext, on_delete=models.CASCADE)

    def __str__(self):
        return self.text.text

    def get_text(self):
        return self.text.text

class Note(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content_plain = models.TextField()
    checklist = models.ForeignKey(Checkcontent, blank=True, null=True, on_delete=models.CASCADE)
    create_date = models.DateField(default=timezone.now().date())
    reminder_date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    tags = MultiSelectField(choices=TAGS, blank=True, null=True)
    alert = models.BooleanField(default=False)

    @property
    def checklist_text(self):
        return self.checklist.get_text()

    @property
    def checklist_checkbox(self):
        return self.checklist.checkbox
    # class Meta:
    #     ordering = ['-create_date']

    def __str__(self):
        return str(self.user.username)
