from django import forms
from .models import GDFile, LocalFile

class GDUploadFileForm(forms.ModelForm):
    class Meta:
        model = GDFile
        fields = ['file']

class LocalUploadFileForm(forms.ModelForm):
    class Meta:
        model = LocalFile
        fields = ['file']

class UploadFileForm(forms.Form):
    file = forms.FileField()
