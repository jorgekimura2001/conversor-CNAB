from django import forms
from .models import FileModel


class FileForm(forms.ModelForm):
    file = forms.FileField()

    class Meta:
        model = FileModel
        fields = '__all__'
