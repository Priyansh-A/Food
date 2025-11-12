import hmac
import hashlib
import base64
import uuid
import json 
from django.views.decorators.csrf import csrf_exempt 
from django.shortcuts import render, get_object_or_404, redirect
from orders.models import Order


def payment_process(request):
    order_id = request.session.get('order_id')
    
    if not order_id:
        return redirect('orders:order_create')
    order = get_object_or_404(Order, id=order_id)
    
    total_amount = str(int(order.get_total_cost()))
    transaction_uuid = uuid.uuid4()
    order.transaction_id = transaction_uuid
    order.save()
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

    
def payment_failure(request):
    return render(request, 'payment/canceled.html')

@csrf_exempt
def payment_success(request):
    encoded_data = request.GET.get('data', '')
    
    if encoded_data:
        try:
            # Decode the base64 data
            decoded_data = base64.b64decode(encoded_data).decode('utf-8')
            transaction_data = json.loads(decoded_data)
            
            # Extract transaction details
            transaction_code = transaction_data.get('transaction_code', '')
            status = transaction_data.get('status', '')
            total_amount = transaction_data.get('total_amount', '')
            transaction_uuid = transaction_data.get('transaction_uuid', '')
            
            # Get order_id from session
            order_id = request.session.get('order_id')
            if order_id:
                order = Order.objects.get(id=order_id)
                
                if status == 'COMPLETE':
                    order.paid = True
                    order.transaction_id = transaction_code
                    order.save()
                    
                    # Clear sessions
                    if 'order_id' in request.session:
                        del request.session['order_id']
                    if 'cart_id' in request.session:  
                        del request.session['cart_id']
                    
                    return render(request, 'payment/completed.html', {
                        'order': order,
                        'transaction_code': transaction_code
                    })
                else:
                    # Payment failed or was incomplete
                    return render(request, 'payment/canceled.html', {
                        'order': order,
                        'status': status
                    })
            else:
                return render(request, 'payment/error.html', {
                    'error': 'Order not found in session'
                })
                
        except Exception as e:
            return render(request, 'payment/error.html', {
                'error': f'Error processing payment: {str(e)}'
            })
    
    return render(request, 'payment/error.html', {
        'error': 'Invalid payment data received'
    })