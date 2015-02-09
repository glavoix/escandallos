from django import forms

from .models import Provider,Product,Measurement,Iva

class ProviderForm(forms.ModelForm):
	class Meta:
		model = Provider
		fields = '__all__'

class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = '__all__'

class MeasurementForm(forms.ModelForm):
	class Meta:
		model = Measurement
		fields = '__all__'

class IvatypeForm(forms.ModelForm):
	class Meta:
		model = Iva
		fields = '__all__'
