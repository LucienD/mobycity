from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _

from carpooling.models import Carpool


class OfferCarpoolForm(forms.ModelForm):
    class Meta:
        model = Carpool

        fields = [
            'departure_latitude',
            'departure_longitude',
            'arrival_latitude',
            'arrival_longitude',
            'frequency',
            'occ_departure_datetime',
            'occ_arrival_datetime',
            'reg_departure_time',
            'reg_arrival_time',
            'seats_number',
            'free',
            'comment',
        ]

        exclude = (
            'organizer',
        )

        widgets = {
            'frequency': forms.RadioSelect(),
            'departure_latitude': forms.HiddenInput(),
            'departure_longitude': forms.HiddenInput(),
            'arrival_latitude': forms.HiddenInput(),
            'arrival_longitude': forms.HiddenInput(),
            'occ_departure_datetime': forms.SplitDateTimeWidget(),
            'occ_arrival_datetime': forms.SplitDateTimeWidget(),
        }
    
    def clean_occ_departure_datetime(self):
        if self.cleaned_data['frequency'] == 'REG':
            return None
        else:
            if (self.cleaned_data['occ_departure_datetime']):
                return self.cleaned_data['occ_departure_datetime']
            else:
                raise ValidationError(_('This field is required.'))

    def clean_occ_arrival_datetime(self):
        if self.cleaned_data['frequency'] == 'REG':
            return None
        else:
            if (self.cleaned_data['occ_arrival_datetime']):
                return self.cleaned_data['occ_arrival_datetime']
            else:
                raise ValidationError(_('This field is required.'))
    
    def clean_reg_departure_time(self):
        if self.cleaned_data['frequency'] == 'OCC':
            return None
        else:
            if (self.cleaned_data['reg_departure_time']):
                return self.cleaned_data['reg_departure_time']
            else:
                raise ValidationError(_('This field is required.'))

    def clean_reg_arrival_time(self):
        if self.cleaned_data['frequency'] == 'OCC':
            return None
        else:
            if (self.cleaned_data['reg_arrival_time']):
                return self.cleaned_data['reg_arrival_time']
            else:
                raise ValidationError(_('This field is required.'))

class SearchCarpoolForm(forms.ModelForm):
    class Meta:
        model = Carpool

        fields = [
            'departure_latitude',
            'departure_longitude',
            'arrival_latitude',
            'arrival_longitude',
            'frequency',
            'occ_arrival_datetime',
            'reg_arrival_time',
        ]

        exclude = (
            'organizer',
        )

        widgets = {
            'frequency': forms.RadioSelect(),
            'departure_latitude': forms.HiddenInput(),
            'departure_longitude': forms.HiddenInput(),
            'arrival_latitude': forms.HiddenInput(),
            'arrival_longitude': forms.HiddenInput(),
            'occ_arrival_datetime': forms.SplitDateTimeWidget(),
        }