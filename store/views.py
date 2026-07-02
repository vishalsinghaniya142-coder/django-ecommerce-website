from django.shortcuts import render
from .models import Product


def home(request):

    search = request.GET.get("search")

    if search:
        products = Product.objects.filter(name__icontains=search)
    else:
        products = Product.objects.all()

    context = {
        "products": products
    }

    return render(request, "home.html", context)


def product_detail(request, id):
    product = Product.objects.get(id=id)

    context = {
        "product": product
    }

    return render(request, "detail.html", context)