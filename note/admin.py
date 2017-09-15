from django.contrib import admin
from .models import Note
# Register your models here.

class NoteModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'create_date']
    list_display_links = ['user', 'title']
    list_filter = ['create_date', 'reminder_date']
    search_fields = ['user__username', 'title', 'content_plain']
    class Meta:
        model = Note
admin.site.register(Note, NoteModelAdmin)
