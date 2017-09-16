from django.db import models
from django.conf import settings
from django.utils import timezone
# why this import?
from multiselectfield import MultiSelectField
# Create your models here.

"""
moving this to a constants file
a constants file should be present in every app and all the constants should be defined there
this will help you when want to change a particular constant and keep the process DRY
"""



# Best Practice: the value of the choice should be less in char length (faster resolution when queries)
TAGS = (('work', 'Work'), #wk
          ('home', 'Home'), #hm
          ('school-college', 'School/College'), #co
          ('hobby', 'Hobby'), #ho
          ('others', 'Others')) #ot

# what if the user wants to create a tag?
# why not have a tag table?



class Note(models.Model):
    # import User model and then assign it. from a readibility presective is easier.
    # like the cascade implementation +1 (+1 = thumbs up)

    user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content_plain = models.TextField()
    create_date = models.DateField(default=timezone.now().date())
    reminder_date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    tags = MultiSelectField(choices=TAGS, blank=True, null=True)
    alert = models.BooleanField(default=False)

    # class Meta:
    #     ordering = ['-create_date']

    def __str__(self):
        return str(self.user.username)


# think of creating an abstract model class for common fields such as
# `at_created`, `by_created`, `at_modified`, `is_active`

# didn't we discuss two types of notes? one a text and other a checklist?