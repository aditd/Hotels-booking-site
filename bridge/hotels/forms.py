from django import forms

locations = [('Kensington and Chelsea', 'Kensington and Chelsea'), ('Westminster Borough', 'Westminster Borough'), ('Central London', 'Central London'), ('Camden', 'Camden'), ('West End', 'West End'), ('Kensington', 'Kensington'), ('Hyde Park', 'Hyde Park'), ('Tower Hamlets', 'Tower Hamlets'), ('Wimbledon', 'Wimbledon'), ('Wandsworth', 'Wandsworth'), ('Newham', 'Newham'), ('Lewisham', 'Lewisham'), ('Clerkenwell', 'Clerkenwell'), ('Stratford', 'Stratford'), ('City of London', 'City of London'), ('Shoreditch', 'Shoreditch'), ('Canary Wharf and Docklands', 'Canary Wharf and Docklands'), ("Regent's Park", "Regent's Park"), ('Spitalfields', 'Spitalfields'), ('Hammersmith and Fulham', 'Hammersmith and Fulham'), ('South Kensington', 'South Kensington'), ('Paddington', 'Paddington'), ('Oxford Street', 'Oxford Street'), ('Wembley', 'Wembley')]
Ratings =(
    (1,"★☆☆☆☆"),
    (2,"★★☆☆☆"),
    (3,"★★★☆☆"),
    (4,"★★★★☆"),
    (5,"★★★★★")
)

class searchForm(forms.Form):
    rating          = forms.IntegerField(required=False,min_value=1,max_value=5)
    neighbourhood   = forms.ChoiceField(choices=locations, widget=forms.RadioSelect,required=False)
    #facilities      = 
    # add a list
    # neighbourhood   = forms.
    price_lower     = forms.IntegerField(required=False,min_value=0)
    price_upper     = forms.IntegerField(required=False,min_value=1)
    smoking_rooms   = forms.BooleanField(required=False)
    pool            = forms.BooleanField(required=False)
    gym             = forms.BooleanField(required=False)
    room_service    = forms.BooleanField(required=False)
    spa             = forms.BooleanField(required=False)
    breakfast       = forms.BooleanField(required=False)
    free_wifi       = forms.BooleanField(required=False)
    dry_cleaning    = forms.BooleanField(required=False)


class RatingForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter your Name'}))
    review = forms.CharField(widget=forms.Textarea)
    rating = forms.ChoiceField(choices = Ratings)
 