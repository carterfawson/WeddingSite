from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm


#import models
from rsvp_app.models import *

#bootstrap login form
class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                                      'class': 'form-control',
                                                      'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                             widget=forms.PasswordInput({
                                                        'class': 'form-control',
                                                        'placeholder':'Password'}))

#all other forms
class RSVP_CodeForm(forms.Form):
    code = forms.CharField(label = False, max_length=20)

class RSVP_Form(forms.Form):
    name = forms.CharField(label = False, max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    email = forms.EmailField(label = False, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    phone = forms.CharField(label = False, max_length=13, widget=forms.TextInput(attrs={'placeholder': 'Phone'}))
    address = forms.CharField(label = False, max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Address'}))
    address2 = forms.CharField(required=False, label = False, max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Address 2'}))
    city = forms.CharField(label = False, max_length=30, widget=forms.TextInput(attrs={'placeholder': 'City'}))
    state = forms.CharField(label = False, max_length=30, widget=forms.TextInput(attrs={'placeholder': 'State'}))
    zip = forms.CharField(label = False, max_length=5, widget=forms.TextInput(attrs={'placeholder': 'Zip'}))
    numguests = forms.IntegerField(label= False, widget=forms.TextInput(attrs={'placeholder': 'Number \'O Guests'}))
    guestnames = forms.CharField(required = False, label = False, widget=forms.Textarea(attrs={'placeholder': 'Guest Names'}))
    comments = forms.CharField(required = False, label= False, widget=forms.Textarea(attrs={'placeholder': 'Questions or Comments'}))

class Advice_Form(forms.Form):
    name = forms.CharField(label = False, max_length=45, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    advice = forms.CharField(required = True, label= False, widget=forms.Textarea(attrs={'placeholder': 'Advice For the Newlyweds OR Travel Suggestions'}))
