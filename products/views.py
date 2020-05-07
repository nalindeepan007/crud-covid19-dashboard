from django.shortcuts import render, get_object_or_404,redirect
from .models import Product
from .forms import ProductForm, RawProductionForm
# Create your views here.

def product_update_view(request, id=id):
    obj = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "product/product_create.html", context)




def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list": queryset

    }
    return render(request, "product/product_list.html", context)


def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj

    }
    return render(request, "product/product_delete.html", context)


def dynamic_lookup_view(request):
    obj = Product.objects.get(id=1)
    context  = {
        "object": obj
    }
    return render(request, "product/product_list.html", context)


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form': form
    }
    return render(request, "product/product_create.html", context)


# def product_detail_view(request):
#     obj = Product.objects.get(id=1)
#
#     context = {
#         'object': obj
#     }
#     return render(request, "product/detail.html", context)

def product_detail_view(request, id):
    obj = get_object_or_404(Product, id=id)
    context = {
        "object": obj
    }
    return render(request, "product/detail.html", context)

# def product_create_view(request):
#     my_form = RawProductionForm()
#     if request.method == "POST":
#
#          my_form = RawProductionForm(request.POST)
#          if my_form.is_valid():
#              print(my_form.cleaned_data)
#              Product.objects.create(**my_form.cleaned_data)
#          else:
#              print(my_form.errors)
#     context = {
#         "form": my_form
#     }
#     return render(request, "product/product_create.html", context)


# def product_create_view(request):
#     # print(request.GET)
#     # print(request.POST)
#     if request.method == "POST":
#           my_new_title = request.POST.get('title')
#           print(my_new_title)
#     context = {}
#     return render(request, "product/product_create.html", context)