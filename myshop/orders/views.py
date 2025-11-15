from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import redirect, render, get_object_or_404
from cart.cart import Cart
from .forms import OrderCreateForm
from .models import OrderItem, Order
import weasyprint
from django.contrib.staticfiles import finders
from django.http import HttpResponse
from django.template.loader import render_to_string

def order_create(request):
    cart = Cart(request)
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if cart.coupon:
                order.coupon = cart.coupon
                order.discount = cart.coupon.discount
            order.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity'],
                )
            cart.clear()
            request.session['order_id'] = order.id
            return redirect('payment:payment_process')
    else:
        form = OrderCreateForm()
    return render(
        request,
            'orders/order/create.html',
            {
            'cart':cart,
            'form': form
            },
        )
    
@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(
        request, 'admin/orders/order/detail.html', {'order':order}
    )
    

@staff_member_required
def admin_order_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    html = render_to_string('orders/order/pdf.html', {'order': order})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'filename=order_{order.id}.pdf'
    # Create HTML object with base_url
    html_obj = weasyprint.HTML(
        string=html,
        base_url=request.build_absolute_uri()
    )
    # Write PDF using explicit keyword arguments
    html_obj.write_pdf(
        target=response,
        stylesheets=[weasyprint.CSS(finders.find('css/pdf.css'))],
    )
    return response