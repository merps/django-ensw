from django import forms
from models import PERReqeust

class RequestForm(forms.ModelForm):

    class Meta:
        model = PERReqeust
