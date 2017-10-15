from django.contrib import admin
from .models import Note, Checkcontent
# Register your models here.

class NoteModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'create_date']
    list_display_links = ['user', 'title']
    list_filter = ['create_date', 'reminder_date', 'user__username', 'last_modified']
    search_fields = ['user__username', 'title', 'content_plain']
    class Meta:
        model = Note

class CheckcontentModelAdmin(admin.ModelAdmin):
    list_display = ['note', 'check_text', 'checkbox']
    raw_id_fields = ['note']

    class Meta:
        model = Checkcontent


admin.site.register(Note, NoteModelAdmin)
admin.site.register(Checkcontent, CheckcontentModelAdmin)
