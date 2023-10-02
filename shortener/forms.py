from django import forms
from shortener.models import Shortener


class ShortenerForm(forms.ModelForm):
    long_url = forms.URLField(widget=forms.URLInput(
        attrs={'class': 'form-control form-control-lg',
               'placeholder': 'Your URLs to Shorten'}
    ))

    class Meta:
        model = Shortener
        fields = ('long_url',)
