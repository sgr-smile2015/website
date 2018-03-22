from django import forms
from .models import RestaurantsLocation


class RestaurantsCreateForm(forms.Form):
    name = forms.CharField()
    location = forms.CharField(required=False)
    category = forms.CharField(required=False)

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name == 'hello':
            raise forms.ValidationError('This not a vilid name')
        return name


class RestaurantsLocationCreateForm(forms.ModelForm):
    class Meta:
        model = RestaurantsLocation
        fields = [
            'name',
            'location',
            'category'
        ]
