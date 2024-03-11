from  django import forms
from django.core.validators import MaxValueValidator,MinValueValidator,MaxLengthValidator,MinLengthValidator,RegexValidator
class my_form(forms.Form):
    name = forms.CharField(max_length=50,validators=[MaxLengthValidator(7)])
    age=forms.IntegerField() 