from django import forms
from .models import UserProfile, Straff

class newPenaltyForm(forms.ModelForm):
    reason = forms.CharField(max_length=80, help_text="Begrunnelse for vinstraff")
    amount = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    to = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    giver = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Category
