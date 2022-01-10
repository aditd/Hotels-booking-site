from django.shortcuts import render, redirect
from .models import Hotel,Photo, Review
from .forms import RatingForm
# Create your views here.


def details_view(request, my_id):    
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            body = {
			'name': form.cleaned_data['name'], 
			'rating': form.cleaned_data['rating'], 
			'review': form.cleaned_data['review']
		    }
            rev = Review(rating=body['rating'], hotel=Hotel.objects.get(id=my_id), review=body['review'])
            rev.save()
            return redirect(f"/hotels/{my_id}")

    form = RatingForm()
    h = Hotel.objects.get(id=my_id)
    photos = h.photo_set.all()
    reviews =h.review_set.all()
    photo_urls =[photo.url for photo in photos]
    facilities = [(h.smoking_rooms, "Smoking Rooms"), (h.pool,"Pool") ,(h.gym, "Gymnasium") ,(h.room_service,"Room Service"), (h.spa, "Spa") ,(h.breakfast, "Breakfast Included") ,(h.free_wifi, "Free Wifi") ,(h.dry_cleaning, "Dry Cleaning Service Offered")]
    context = {
        'reviews':reviews,
        'form':form,
        'object':h,
        'urls': photo_urls,
        'facilities':facilities
    }
    return render(request,"details.html",context)
