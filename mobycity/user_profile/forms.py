from django import forms

from user_profile.models import UserProfile


class PictureForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        
        fields = [
            'picture',
        ]
        
        exclude = (
            'user',
            'phone',
        )
    
    
class PhoneForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        
        fields = [
            'phone',
        ]
        
        exclude = (
            'user',
            'picture',
        )