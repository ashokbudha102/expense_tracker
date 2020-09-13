from django import forms
from functools import partial
DateInput=partial(forms.DateInput, {'class':'datepicker'})

class downloadForm(forms.Form):
    startingDate = forms.DateField(widget=DateInput())
    endingDate = forms.DateField(widget=DateInput())

