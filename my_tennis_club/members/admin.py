from django.contrib import admin
from .models import Member

# Register your models here.

# This is to show the models in django admin console
#admin.site.register(Member)

# we can control the fields to display by specifying them in in a list_display property in the admin.py file.
# first create a MemberAdmin() class and specify the list_display tuple
class MemberAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "joined_date",)

# This is to show the models in django admin console
admin.site.register(Member, MemberAdmin)