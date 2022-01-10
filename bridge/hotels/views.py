from django.shortcuts import render
from .models import Hotel,Photo
# Create your views here.

def details_view(request, my_id):
    h = Hotel.objects.get(id=my_id)
    photos = h.photo_set.all()
    photo_urls =[photo.url for photo in photos]
    facilities = [(h.smoking_rooms, "Smoking Rooms"), (h.pool,"Pool") ,(h.gym, "Gymnasium") ,(h.room_service,"Room Service"), (h.spa, "Spa") ,(h.breakfast, "Breakfast Included") ,(h.free_wifi, "Free Wifi") ,(h.dry_cleaning, "Dry Cleaning Service Offered")]
    context = {
        'object':h,
        'urls': photo_urls,
        'facilities':facilities
    }
    return render(request,"details.html",context)
