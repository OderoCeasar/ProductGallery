from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm

# Show all products
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

# create products
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
    return render(request, 'products/product_form.html', {'form': form, 'action': 'Add'})

# update products
def product_update(request, pk):
    product = get_object_or_404(Product, id=pk)
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
    return render(request, 'products/product_form.html', {'form': form, 'action': 'Edit'})

# delete products
def product_delete(request, pk):
    product = get_object_or_404(Product, id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'products/product_confirm_delete.html', {'product': product})
