#coding:utf-8

from django import forms


class ContactForm(forms.Form):
    last_name = forms.CharField(max_length=100, label=u'Nom')
    first_name = forms.CharField(max_length=100, label=u'Prénom')
    email = forms.EmailField(label=u'E-mail')
    subject = forms.CharField(max_length=255, label=u'Objet')
    message =  forms.CharField(widget=forms.Textarea, label=u'Message')