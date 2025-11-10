from django.shortcuts import render, get_object_or_404
from django_esewa import EsewaPayment
from orders.models import Order, OrderItem
import uuid

def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    
    uid = uuid.uuid4()
    epayment = EsewaPayment(
        product_code= "EPAYTEST",
        success_url=request.build_absolute_uri('/payment/completed/'),
        failure_url=request.build_absolute_uri('/payment/canceled/'),
        secret_key='8gBm/:&EnhH.1/q',
    )
    epayment.create_signature(
        amount=order.get_total_cost(),
        transaction_uuid=str(uid)
    )
    context = {
        'product': OrderItem.product,
        'form': epayment.generate_form(),
    }
    return render(request, 'payment/process.html', context)

def payment_success(request):
    return render(request, 'payment/completed.html')
    
def payment_failure(request):
    return render(request, 'payment/canceled.html')