from django import forms

Ratings =(
    (1,"1"),
    (2,"2"),
    (3,"3"),
    (4,"4"),
    (5,"5")
)
  


class RatingForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter your Name'}))
    review = forms.CharField(widget=forms.Textarea)
    rating = forms.ChoiceField(choices = Ratings)
