from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

#create product
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = Product(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                price=form.cleaned_data['price']
            )
            if request.FILES.get('image'):
                product.image.put(request.FILES['image'], content_type=request.FILES['image'].content_type)
            product.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'products/product_form.html', {'form': form})


#update product
def product_update(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product.name = form.cleaned_data['name']
            product.description = form.cleaned_data['description']
            product.price = form.cleaned_data['price']
            if request.FILES.get('image'):
                product.image.replace(request.FILES['image'], content_type=request.FILES['image'].content_type)
            product.save()
            return redirect('product_list')
    else:
        form = ProductForm(initial={
            'name': product.name,
            'description': product.description,
            'price': product.price
        })
    return render(request, 'products/product_form.html', {'form': form})


#delete product
def product_delete(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return redirect('product_list')
