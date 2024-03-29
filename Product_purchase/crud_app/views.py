from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product
@login_required(login_url='login_url')
def create_order(request):
    template_name = 'crud_app/create.html'
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_url")

    context = {'form': form}
    return render(request, template_name, context)

@login_required(login_url='login_url')
def show_order(request):
    template_name = 'crud_app/show.html'
    products = Product.objects.all()
    context = {'products': products}
    return render(request, template_name, context)

def update_order(request, pk):
    template_name = 'crud_app/create.html'
    obj = Product.objects.get(id=pk)
    form = ProductForm(instance=obj)
    if request.method == "POST":
        form = ProductForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect("show_url")
    context = {'form': form}
    return render(request, template_name, context)

def cancel_order(request, pk):
    template_name = 'crud_app/confirm.html'
    obj = Product.objects.get(id=pk)
    if request.method == "POST":
        obj.delete()
        return redirect("show_url")
    return render(request, template_name)