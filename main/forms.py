from django import forms
from functools import partial
from .models import Expense
DateInput=partial(forms.DateInput, {'class':'datepicker'})

class downloadForm(forms.Form):
    startingDate = forms.DateField(widget=DateInput())
    endingDate = forms.DateField(widget=DateInput())



class ExpenseForm(forms.ModelForm):
    """Form definition for MODELNAME."""
    date=forms.DateField(widget=DateInput())

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = Expense
        fields = ('description','amount','date','category')
    