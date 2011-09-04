from django import forms
from grajteka import models

class TransferForm(forms.Form):
	boardgame_id = forms.IntegerField(widget=forms.HiddenInput)
	person_new_username = forms.CharField(widget=forms.TextInput(attrs={'onkeypress':'return autocomplete(this, event, arrValues)',}))
	transfer_type = forms.CharField(widget=forms.Select(choices=models.TRANSFER_TYPES))
	desc = forms.CharField( widget=forms.Textarea(attrs={'cols':40,'rows':3,}),required=False)

event_choices = [(e.id, e.title) for e in models.Event.objects.all()]

class EventChangeForm(forms.Form):
	#event_choices = [(e.title) for e in models.Event.objects.all()]
	event_id = forms.CharField(widget=forms.Select(choices=event_choices))
	#event_new = forms.CharField(widget=forms.Select)
