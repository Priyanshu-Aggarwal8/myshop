from django import forms 

class FeedbackForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()