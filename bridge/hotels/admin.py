from django.contrib import admin

# Register your models here.
from .models import Hotel, Photo, Review

admin.site.register(Hotel)
admin.site.register(Photo)
admin.site.register(Review)
