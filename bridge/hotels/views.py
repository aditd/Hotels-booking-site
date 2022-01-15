from django.shortcuts import render, redirect
from .models import Hotel,Photo, Review
from .forms import RatingForm, searchForm
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

def hotel_search_view(request): 
    x = Hotel.objects.all()

    if request.method == "GET":
        form = searchForm(request.GET)
        # if the form is valid
        if form.is_valid():
            # facilities
            x = x.filter(smoking_rooms=True) if form.cleaned_data['smoking_rooms'] == True else x
            x = x.filter(pool=True) if form.cleaned_data['pool'] == True else x
            x = x.filter(free_wifi=True) if form.cleaned_data['free_wifi'] == True else x
            x = x.filter(gym=True) if form.cleaned_data['gym'] == True else x
            x = x.filter(spa=True) if form.cleaned_data['spa'] == True else x
            x = x.filter(dry_cleaning=True) if form.cleaned_data['dry_cleaning'] == True else x
            x = x.filter(room_service=True) if form.cleaned_data['room_service'] == True else x
            x = x.filter(breakfast=True) if form.cleaned_data['breakfast'] == True else x

            if form.cleaned_data['price_lower'] != None:
                x=x.filter(price__gt=form.cleaned_data['price_lower'])

            if form.cleaned_data['price_upper'] != None:
                x=x.filter(price__lt=form.cleaned_data['price_upper'])
            
            if form.cleaned_data['price_lower'] != None:
                x=x.filter(price__gt=form.cleaned_data['price_lower'])

            #if the rating field isnt filled
            if form.cleaned_data['rating'] != None:
                y = []
                # search every hotel and check if it has that rating. after this we get a list y with hotels of that rating
                for hotel in x:
                    # if the hotel has an average rating of what is asked
                    if hotel.review_set.all():
                        if hotel.average_rating()==form.cleaned_data['rating']:
                            y.append(hotel)
                # x needs to be put into the context
                x=y
                
        #form = searchForm()
        context = {
        "hotels": x,
        "form": form
        }
        return render(request,"search.html", context)
   
        