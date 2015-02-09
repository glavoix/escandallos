from django.contrib import admin

# Register your models here.

from .models import Provider,Product,Measurement,Iva

class ProviderAdmin(admin.ModelAdmin):
	class Meta:
	 model = Provider


class ProductAdmin(admin.ModelAdmin):
	class Meta:
	 model = Product

	 
class MeasurementAdmin(admin.ModelAdmin):
	class Meta:
	 model = Measurement


admin.site.register(Product,ProviderAdmin)
admin.site.register(Provider,ProviderAdmin)
admin.site.register(Measurement,ProviderAdmin)
