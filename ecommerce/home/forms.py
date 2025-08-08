from django import forms
from .models import Home, FileFields

class DjangoForms(forms.Form):
    Name = forms.CharField(max_length=100, label="Name")
    Email = forms.EmailField(max_length=100, label="Email")
    Addrs = forms.CharField(max_length=100, label="Address")
    Contact = forms.IntegerField(label="Contact")


class ModelForms(forms.ModelForm):
    class Meta:
        model = Home
        # fields = ['Name', 'Field', 'Quality', 'Item_ID', 'Image']
        fields = '__all__'
        # exclude = ['Image']

class ImageForm(forms.ModelForm):
    class Meta:
        model= FileFields
        fields = '__all__'