from django.contrib import admin

# Register your models here.
from .models import Hotel, Photo

admin.site.register(Hotel)
admin.site.register(Photo)