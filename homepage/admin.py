from django.contrib import admin
from .models import UserProfile


# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'register')
    list_filter = ('register',)
    search_fields = ('name', 'phone_number')


admin.site.register(UserProfile, UserProfileAdmin)
