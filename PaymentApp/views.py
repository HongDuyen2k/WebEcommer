from urllib import request
from django.shortcuts import redirect, render
from models.models import *
from django.utils.crypto import get_random_string
from django.contrib import messages
import stripe
from django.conf import settings
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.views import View


stripe.api_key = settings.STRIPE_SECRET_KEY

def payment_success(request):
    current_uer = request.user
    carts = Cart.objects.filter(user_id=current_uer.id, status='Draft')
    order = Order.objects.get(user_id=current_uer.id, status='Draft')
        
    for cart in carts:
        data= Cart.objects.get(id=cart.id)

        order_cart = OrderCart()
        order_cart.order_id = order.id
        order_cart.cart_id = data.id
        order_cart.save()
            
        data.status = 'Done'
        data.save()
        
    payment = Payment()
    payment.codeBill = get_random_string(length=32)
    payment.price = order.totalPriceAfter
    payment.order_id = order.id
    payment.save()

    order.status = 'Pending'
    order.save()
    messages.success(request, 'Bạn đã đặt hàng thành công')
    return redirect('general_home')

def payment_cancel(request):
    messages.warning(request, 'Bạn đã đặt hàng không thành công')
    return redirect('general_home')

class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        user_id = self.kwargs["pk"]
        order = Order.objects.get(user_id=user_id, status='Draft')
        name = get_random_string(length=32)
        YOUR_DOMAIN = "http://127.0.0.1:8000"
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'VND',
                        'unit_amount': order.totalPriceAfter,
                        'product_data': {
                            'name': name,
                        },
                    },
                    'quantity': 1,
                },
            ],
            metadata={
                "order_id": order.id,
                "user_id": user_id
            },
            mode='payment',
            success_url=YOUR_DOMAIN + '/payment-success/',
            cancel_url=YOUR_DOMAIN + '/payment-cancel/',
        )
        return JsonResponse({
            'id': checkout_session.id
        })


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
    
    elif event["type"] == "payment_intent.succeeded":
        intent = event['data']['object']
        order_id = intent["metadata"]["order_id"]
        user_id = intent["metadata"]["user_id"]

        carts = Cart.objects.filter(user_id=user_id, status='Draft')
        order = Order.objects.get(user_id=user_id, status='Draft')
            
        for cart in carts:
            data= Cart.objects.get(id=cart.id)

            order_cart = OrderCart()
            order_cart.order_id = order.id
            order_cart.cart_id = data.id
            order_cart.save()
                
            data.status = 'Done'
            data.save()

        payment = Payment()
        payment.codeBill = get_random_string(length=32)
        payment.price = order.totalPriceAfter
        payment.order_id = order.id
        payment.save()

        order.status = 'Pending'
        order.save()

    return HttpResponse(status=200)