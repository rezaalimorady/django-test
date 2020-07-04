from django.contrib import admin
from .models import Upload
from django_jalali.admin.filters import JDateFieldListFilter


# Register your models here.

class UploadAdmin(admin.ModelAdmin):
    list_display = ('title', 'request_user', 'organ', 'date',)
    list_filter = ('organ', ('date', JDateFieldListFilter),)
    search_fields = ('title', 'description', 'name')


admin.site.register(Upload, UploadAdmin)
