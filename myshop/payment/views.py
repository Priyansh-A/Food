import hmac
import hashlib
import base64
import uuid
from django.shortcuts import render, get_object_or_404, redirect
from orders.models import Order


def payment_process(request):
    order_id = request.session.get('order_id')
    
    if not order_id:
        return redirect('orders:order_create')
    order = get_object_or_404(Order, id=order_id)
    
    total_amount = str(int(order.get_total_cost()))
    transaction_uuid = uuid.uuid4()
    product_code = "EPAYTEST"
    data_to_sign = f"total_amount={total_amount},transaction_uuid={transaction_uuid},product_code={product_code}"
    
    secret = "8gBm/:&EnhH.1/q".encode()

    message = data_to_sign
    hmac_sha256 = hmac.new(secret, message.encode('utf-8'), hashlib.sha256)
    signature = base64.b64encode(hmac_sha256.digest()).decode('utf-8')

    
    signed_field_names = "total_amount,transaction_uuid,product_code"
    
    success_url = "http://127.0.0.1:8000/payment/completed/"
    failure_url = "http://127.0.0.1:8000/payment/canceled/"

    context = {
        'order': order,
        'total_amount': total_amount,
        'transaction_uuid': transaction_uuid,
        'product_code': product_code,
        'signature': signature,
        'signed_field_names': signed_field_names,
        'success_url': success_url,
        'failure_url': failure_url,
    }
    
    return render(request, 'payment/process.html', context)


def payment_success(request):
    return render(request, 'payment/completed.html')
    
def payment_failure(request):
    return render(request, 'payment/canceled.html')