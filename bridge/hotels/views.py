from django.shortcuts import render, redirect
from .models import Hotel,Photo, Review
from .forms import RatingForm, searchForm

# possible london locations
#location = ["Kensington and Chelsea","Westminster Borough","Central London","Camden","West End","Kensington","Hyde Park","Tower Hamlets","Wimbledon","Wandsworth","Newham","Lewisham","Clerkenwell","Stratford","City of London","Shoreditch","Canary Wharf and Docklands","Regent's Park","Spitalfields","Hammersmith and Fulham","South Kensington","Paddington","Oxford Street","Wembley"]

# this helps in suggesting places withing a price range
def priceRange(price):
	diff = 1000
	h = Hotel.objects.all()
	h = h.filter(price__gt=price-diff)
	h = h.filter(price__lt=price+diff)
	return h[:4]

def searchFunctionality(smoking_rooms,pool,free_wifi,gym, spa, dry_cleaning, room_service, breakfast):
	x = Hotel.objects.all()
	x = x.filter(smoking_rooms=True) if smoking_rooms == True else x
	x = x.filter(pool=True) if pool == True else x
	x = x.filter(free_wifi=True) if free_wifi else x
	x = x.filter(gym=True) if gym else x
	x = x.filter(spa=True) if spa else x
	x = x.filter(dry_cleaning=True) if dry_cleaning else x
	x = x.filter(room_service=True) if room_service else x
	x = x.filter(breakfast=True) if breakfast else x

	return x

# Create your views here.
def homeView(request):
	context = {}
	return render(request,"home.html",context)


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
	similar = priceRange(h.price)
	photos = h.photo_set.all()
	reviews =h.review_set.all()
	photo_urls =[photo.url for photo in photos]
	facilities = [(h.smoking_rooms, "Smoking Rooms"), (h.pool,"Pool") ,(h.gym, "Gymnasium") ,(h.room_service,"Room Service"), (h.spa, "Spa") ,(h.breakfast, "Breakfast Included") ,(h.free_wifi, "Free Wifi") ,(h.dry_cleaning, "Dry Cleaning Service Offered")]
	context = {
		'reviews':reviews,
		'form':form,
		'object':h,
		'urls': photo_urls,
		'facilities':facilities,
		'recommendations':similar
	}
	return render(request,"details.html",context)





def hotel_search_view(request): 
	x = Hotel.objects.all()

	if request.method == "GET":
		form = searchForm(request.GET)
		# if the form is valid
		if form.is_valid():
			# facilities
			#facilities = [form.cleaned_data['smoking_rooms'],form.cleaned_data['pool'],form.cleaned_data['free_wifi'], form.cleaned_data['gym'],form.cleaned_data['spa'],form.cleaned_data['dry_cleaning'],form.cleaned_data['room_service'],form.cleaned_data['breakfast']]
			x=searchFunctionality(form.cleaned_data['smoking_rooms'],form.cleaned_data['pool'],form.cleaned_data['free_wifi'], form.cleaned_data['gym'],form.cleaned_data['spa'],form.cleaned_data['dry_cleaning'],form.cleaned_data['room_service'],form.cleaned_data['breakfast'])

			if form.cleaned_data['price_lower'] != None:
				x=x.filter(price__gt=form.cleaned_data['price_lower'])

			if form.cleaned_data['price_upper'] != None:
				x=x.filter(price__lt=form.cleaned_data['price_upper'])
			
			if form.cleaned_data['neighbourhood'] != None:
				x=x.filter(address__icontains=form.cleaned_data['neighbourhood'])

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
   
		