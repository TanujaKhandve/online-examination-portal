from django.contrib import admin # type: ignore

# Register your models here.
from django.contrib import admin # type: ignore
from .models import ContactMessage

admin.site.register(ContactMessage)
