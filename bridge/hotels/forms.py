from django import forms

Ratings =(
    (1,"★☆☆☆☆"),
    (2,"★★☆☆☆"),
    (3,"★★★☆☆"),
    (4,"★★★★☆"),
    (5,"★★★★★")
)

class searchForm(forms.Form):
    rating          = forms.IntegerField(required=False,min_value=1,max_value=5)
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
 