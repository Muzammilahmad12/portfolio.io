from django.contrib import admin
from Contact.models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name' , 'email' , 'subject' , 'message' , 'date_submitted')