from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from CategoryApp.views import *
from GeneralApp.views import *
from UserApp.views import *
from ClothesApp.views import *
from CartApp.views import *
from OrderApp.views import *
from PaymentApp.views import *
from FeedbackApp.views import *
from PhoneApp.views import *

urlpatterns = [
    ## GeneralApp
    path('', general_home, name='general_home'),
    path('search', general_search_product, name='general_search_product'),

    ## UserApp
    path('user/user-login', user_login, name='user_login'),
    path('user/user-register', user_register, name='user_register'),
    path('user/user-logout', user_logout, name='user_logout'),
    path('user/user-profile', user_profile, name='user_profile'),

    ## PhoneApp
    path('phone/add-now/<int:id>/', phone_add_now_cart, name='phone_add_now_cart'),
    path('phone/phone-details/<int:id>', phone_details, name='phone_details'),

    ## ClothesApp
    path('clothes/add-now/<int:id>/', clothes_add_now_cart, name='clothes_add_now_cart'),
    path('clothes/clothes-details/<int:id>', clothes_details, name='clothes_details'),

    ## CartApp
    path('cart/cart-details', cart_details, name='cart_details'),
    path('cart/cart-delete/<int:id>', cart_delete, name='cart_delete'),

    ## OrderApp
    path('order/order-cart-product', order_cart_product, name='order_cart_product'),
    path('order/order-confirm-before', order_confirm_before, name='order_confirm_before'),
    path('order/order-details', order_details, name='order_detail'),

    ## CategoryApp
    path('category/category-show/<str:category>/<int:id>', category_show_by_category, name='category_show_by_category'),

    ## FeedbackApp
    path('feedback/feedback-add/<str:category>/<int:id>', feedback_add, name='feedback_add'),

    ## PaymentApp
    path('payment/payment-now', payment_success, name='payment_now'),
    path('webhooks/stripe/', stripe_webhook, name='stripe-webhook'),
    path('payment-cancel/', payment_cancel, name='payment_cancel'),
    path('payment-success/', payment_success, name='payment_success'),
    path('create-checkout-session/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)