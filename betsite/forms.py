from django.forms import ModelForm
from django import forms
from .models import Deposit, Placebet

class DepositForm(forms.ModelForm):
    class Meta:
        model = Deposit
        fields = ('mobile_number', 'user_id', 'amount')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['mobile_number'].widget.attrs['placeholder'] = ' Mobile Number'
        self.fields['user_id'].widget.attrs['placeholder'] = ' User ID'
        self.fields['amount'].widget.attrs['placeholder'] = ' Amount'

class PlacebetForm(forms.ModelForm):
    class Meta:
        model = Placebet
        fields = ('game_id', 'amount', 'prediction')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['game_id'].widget.attrs['placeholder'] = ' Game ID'
        self.fields['amount'].widget.attrs['placeholder'] = ' Amount'
        self.fields['prediction'].widget.attrs['placeholder'] = ' Prediction'
