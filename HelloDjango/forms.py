#-*-coding: utf-8*-
from django import forms

class profileForm(forms.form):
    name = forms.CharField(max_length=100)
    picture = forms.ImageField()
    