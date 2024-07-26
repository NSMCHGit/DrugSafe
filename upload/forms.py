
from django import forms
from upload.models import Image
from upload.models import Document


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('image',)

class DocForm(forms.ModelForm):
	class Meta:
		model=Document
		fields="__all__"
