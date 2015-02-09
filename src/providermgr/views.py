from django.shortcuts import render, render_to_response, RequestContext

from .forms import ProviderForm,ProductForm,IvatypeForm,MeasurementForm

from .models import Product,Provider

# Create your views here.

def home(request):
        products = Product.objects.all()
        form = ProviderForm(request.POST or None)
        if form.is_valid():
          save_it = form.save(commit=False)
          save_it.save()



	return render_to_response("home.html",
					locals(),
					context_instance=RequestContext(request))

def aboutus(request):
	return render_to_response("home.html",
                                        locals(),
                                        context_instance=RequestContext(request))
def addproduct(request):
          form = ProductForm(request.POST or None)

          if form.is_valid():
            save_it = form.save(commit=False)
            save_it.save()
          return render_to_response("add_product.html",
                                        locals(),
                                        context_instance=RequestContext(request))
def listproducts(request):
          products = Product.objects.all()
          #measure = Product.objects.all().prefetch_related('measurementtype_id')
        
          return render_to_response("listproducts.html",
                                        locals(),
                                        context_instance=RequestContext(request))


def ivatype(request):
          form = IvatypeForm(request.POST or None)

          if form.is_valid():
            save_it = form.save(commit=False)
            save_it.save()
          return render_to_response("add_product.html",
                                        locals(),
                                        context_instance=RequestContext(request))

def add_measurement(request):
          form = MeasurementForm(request.POST or None)

          if form.is_valid():
            save_it = form.save(commit=False)
            save_it.save()
          return render_to_response("add_measurement.html",
                                        locals(),
                                        context_instance=RequestContext(request))




def addrecipe(request):
          form = RecipeForm(request.POST or None)

          if form.is_valid():
            save_it = form.save(commit=False)
            save_it.save()
          return render_to_response("addrecipe.html",
                                        locals(),
                                        context_instance=RequestContext(request))