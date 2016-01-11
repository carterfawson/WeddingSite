from django.contrib import admin

# Register your models here.

from .models import contact, advice

admin.site.register(contact)
admin.site.register(advice)
