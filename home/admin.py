from django.contrib import admin
from .models import Contact

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    listt_display = ("FirstName", "LastName", "Email", "ContactNumber")
admin.site.register(Contact,ContactAdmin)    