from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'primary_phone_number': 'Phone Number',
            'primary_postcode': 'Postal Code',
            'primary_town_or_city': 'Town or City',
            'primary_street_address1': 'Street Address 1',
            'primary_street_address2': 'Street Address 2',
            'primary_county': 'County, State or Area',
        }

        self.fields['primary_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'primary_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'profile-input-style'
            self.fields[field].label = False
