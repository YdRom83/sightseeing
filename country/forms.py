from django.forms import ModelForm
from country.models import Country


class CountryForm(ModelForm):

    class Meta:
        model = Country
        fields = ("title", "description", "image", "url")
        
        