from django.contrib import admin

# Register your models here.

from .models import CreateFile,Signature

admin.site.register(CreateFile)
admin.site.register(Signature)