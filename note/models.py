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
    # checklist = models.ForeignKey(Checkcontent, blank=True, null=True, on_delete=models.CASCADE)
    create_date = models.DateField(default=timezone.now().date())
    reminder_date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    last_modified = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True, null=True)
    tags = MultiSelectField(choices=TAGS, blank=True, null=True)
    alert = models.BooleanField(default=False)

    # @property
    # def checklist_text(self):
    #     if self.checklist != None:
    #         return self.checklist.get_text()
    #
    # @property
    # def checklist_checkbox(self):
    #     if self.checklist != None:
    #         return self.checklist.checkbox
    # class Meta:
    #     ordering = ['-create_date']

    def __str__(self):
        return str(self.user.username)

# class Checktext(models.Model):
#     # note = models.ForeignKey(Note, related_name='checklists', default=0, on_delete=models.CASCADE)
#     checkbox = models.BooleanField(default=False, unique=True)
#     # check_text = models.ForeignKey(Checktext, default="", to_field='text', on_delete=models.CASCADE)
#
#     # def __str__(self):
#     #     return self.check_text.text
#     #
#     # def get_text(self):
#     #     return self.check_text.text


class Checkcontent(models.Model):
    note = models.ForeignKey(Note, related_name='checklists', default=0, on_delete=models.CASCADE)
    check_text = models.CharField(max_length=60, default=" ")
    checkbox = models.BooleanField(default=False)

    def __str__(self):
        return self.check_text


# handle null on text - done
# handle update view
