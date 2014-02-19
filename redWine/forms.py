from django import forms
from .models import UserProfile, Straff

class newPenaltyForm(forms.ModelForm):
    reason = forms.CharField(help_text="Begrunnelse for vinstraff")
    amount = forms.IntegerField( initial=0)
    to = forms.IntegerField(widget=forms.HiddenInput())
    giver = forms.CharField(widget=forms.HiddenInput())

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Straff
