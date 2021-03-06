from django.db import models
from django.utils.encoding import smart_unicode
# Create your models here.

class Provider(models.Model):
        provider_name = models.CharField(max_length=120, null=False, blank=False, unique=True)
        provider_addr = models.CharField(max_length=120, null=True, blank=True)
        provider_phone = models.CharField(max_length=20, null=True, blank=True)
        timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
        updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return smart_unicode(self.provider_name)

class Iva(models.Model):
	iva_type = models.IntegerField(default=10, null=False, blank=False, unique=True)
        def __unicode__(self):
                return smart_unicode(self.iva_type)

class Measurement(models.Model):
	measurement_type = models.CharField(max_length=20, null=False, blank=False, unique=True)
        def __unicode__(self):
                return smart_unicode(self.measurement_type)
class Product(models.Model):
        product_name = models.CharField(max_length=120, null=True, blank=True)
	prov_name = models.ForeignKey(Provider)
	product_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
	ivatype =  models.ForeignKey(Iva)
        recipient_size = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)  
        measurementtype = models.ForeignKey(Measurement)
        timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
        updated = models.DateTimeField(auto_now_add=False, auto_now=True)
        comment = models.CharField(max_length=120, null=True, blank=True)

	def __unicode__(self):
		return smart_unicode(self.product_name)

class Recipe(models.Model):
        recipe_name = models.CharField(max_length=120, null=True, blank=True)


