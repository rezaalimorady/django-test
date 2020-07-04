from django.contrib import admin
from .models import Message


# Register your models here.

class MessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'update')
    list_filter = ('date', 'update', )
    search_fields = ('title', 'description')


admin.site.register(Message, MessageAdmin)
