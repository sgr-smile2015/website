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
    #mail = forms.EmailField()

    class Meta:
        model = RestaurantsLocation
        fields = [
            'name',
            'location',
            'category',
            'mail'
        ]

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name == 'hello':
            raise forms.ValidationError('not accept hello name')
        return name

    def clean_mail(self):
        email = self.cleaned_data.get("mail")
        if 'qq.com' in email:
            raise forms.ValidationError('not accept qq email')
        return email
