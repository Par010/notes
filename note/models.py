from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=30)
    content_plain = models.TextField()
    create_date = models.DateField(auto_now_add=True)
    reminder_date = models.DateTimeField(auto_now=False, auto_now_add=False)
