from django import forms
from django_countries.fields import CountryField
from . import models


class SearchForm(forms.Form):

    """ Search Form Definition """

    city = forms.CharField(initial="Anywhere")
    countries = CountryField(blank=True, default="KR").formfield()
    room_type = forms.ModelChoiceField(
        empty_label="Any kind", queryset=models.RoomType.objects.all(), required=False
    )
    price = forms.IntegerField(required=False)
    guests = forms.IntegerField(required=False)
    bedroomss = forms.IntegerField(required=False)
    beds = forms.IntegerField(required=False)
    baths = forms.IntegerField(required=False)
    instant_book = forms.BooleanField(required=False)
    superhost = forms.BooleanField(required=False)
    amenities = forms.ModelMultipleChoiceField(
        queryset=models.Amenity.objects.all(), widget=forms.CheckboxSelectMultiple
    )
    facilities = forms.ModelMultipleChoiceField(
        queryset=models.Facility.objects.all(), widget=forms.CheckboxSelectMultiple
    )
