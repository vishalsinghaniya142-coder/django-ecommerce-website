from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from cart.models import Cart
from .models import Order


@login_required
def place_order(request):

    cart_items = Cart.objects.filter(user=request.user)

    for item in cart_items:

        Order.objects.create(
            user=request.user,
            product=item.product,
            quantity=item.quantity,
            total_price=item.product.price * item.quantity
        )

    cart_items.delete()

    return redirect("order_success")
from django.shortcuts import render
@login_required
def order_success(request):
    return render(request, "order_success.html")
@login_required
def order_history(request):

    orders = Order.objects.filter(user=request.user).order_by("-ordered_at")

    return render(request, "order_history.html", {
        "orders": orders
    })