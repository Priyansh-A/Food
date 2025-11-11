import uuid
import hmac
import hashlib
import base64
from django.shortcuts import render, get_object_or_404
from orders.models import Order


def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    
    total_amount = str(int(order.get_total_cost()))
    transaction_uuid = str(uuid.uuid4())
    
    product_code = 'EPAYTEST'
    secret_key = '8gBm/:&EnhH.1/q'
    
    data_to_sign = f"total_amount={total_amount},transaction_uuid={transaction_uuid},product_code={product_code}"
    
    secret = secret_key.encode('utf-8')
    message = data_to_sign.encode('utf-8')
    hmac_sha256 = hmac.new(secret, message, hashlib.sha256)
    digest = hmac_sha256.digest()
    signature = base64.b64encode(digest).decode('utf-8')
    
    signed_field_names = "total_amount,transaction_uuid,product_code"

    context = {
        'total_amount': total_amount,
        'transaction_uuid': transaction_uuid,
        'product_code': product_code,
        'signature': signature,
        'signed_field_names': signed_field_names,
        'data_to_sign': data_to_sign,
    }

    return render(request, 'process.html', context)

def payment_success(request):
    return render(request, 'payment/completed.html')
    
def payment_failure(request):
    return render(request, 'payment/canceled.html')