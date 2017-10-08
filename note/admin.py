from django.contrib import admin
from .models import Note, Checkcontent, Checktext
# Register your models here.

class NoteModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'create_date']
    list_display_links = ['user', 'title']
    list_filter = ['create_date', 'reminder_date', 'user__username']
    search_fields = ['user__username', 'title', 'content_plain']
    class Meta:
        model = Note

class CheckcontentModelAdmin(admin.ModelAdmin):
    list_display = ['check_text', 'checkbox', 'note']

    class Meta:
        model = Checkcontent


admin.site.register(Note, NoteModelAdmin)
admin.site.register(Checkcontent, CheckcontentModelAdmin)
admin.site.register(Checktext)
