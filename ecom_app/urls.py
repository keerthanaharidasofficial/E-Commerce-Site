from django.urls import path
from .views import *    # * is a universal symbol

urlpatterns = [
    path('e-commerce-1-index-page/',my_ecom_index),
    path('e-com-1-navbar/',ecom_navbar),
    path('e-com-1-fashion-page/',my_ecom_fashion),
    path('e-com-1-jewellery-page/',my_ecom_jewellery),
    path('e-com-1-login-page-for-sellers/',my_ecom_login_seller),
    path('e-com-1-register-page-for-sellers/', my_ecom_register_seller),
    path('e-com-1-display-seller-data/',ecom_display),
    path('e-com-1-edit-seller-register-data/<int:id>',edit_ecom_seller_register),
    path('e-com-1-edit-seller-product-data/<int:id>',edit_ecom_seller_products),
    path('e-com-1-delete-seller-register-data/<int:id>',delete_ecom_seller_reg_data),
    path('e-com-1-delete-seller-product-data/<int:id>',delete_seller_products),
    path('e-com-1-upload-seller-products-details/<int:login_id>',ecom_sellerproduct_upload),
    path('e-com-1-profile-page/',profile_page),
    path('e-com-1-products-display-page/<int:id>',prod_display_seller),
#     --------------------- BUYER -----------------------------------------------------
    path('e-com-1-login-page-for-buyer/', my_ecom_login_buyer),
    path('e-com-1-register-page-for-buyers/', my_ecom_register_buyer),
    path('e-com-1-eflyer--profile-page-user/', user_profile_page),
    path('e-com-1-eflyer--profile-page-user-logout/', user_logout),
    path('e-com-1-eflyer--profile-page-seller-logout/', seller_logout),
    path('e-com-1-user-wishlist-items/<int:id>',user_wishlist_items),
    path('e-com-1-display-user-wishlist-items/',user_wishlist_display),
    path('e-com-1-delete-user-wishlist-items/<int:id>',wishlist_item_remove),
    path('e-com-1-user-cart-items/<int:id>',user_cart_items),
    path('e-com-1-display-user-cart-items/',user_cart_display),
    path('e-com-1-delete-user-cart-items/<int:id>',cart_item_remove),
    path('e-com-1-buyer-proceed-to-buy-items-page-1/<int:id>',proceed_buy_1),
    path('e-com-1-buyer-proceed-to-buy-confirm-address-page-2/<int:id>',proceed_buy_2),
    path('e-com-1-buyer-edit-delivery-address/<int:id>',edit_delivery_address),
    path('e-com-1-buyer-delete-delivery-address/<int:id>',delete_delivery_address),
    path('e-com-1-user-payment-details/<int:id>',user_payment),
    path('e-com-1-user-my-order-details/',my_orders),
    path('e-com-1-user-my-order-display/',my_orders_display),
    path('e-com-1-clear-user-my-order-history/',clear_order_history),
    # -------------------------------AUTHORISED USER/ADMIN FORM-------------------------------------
    path('e-com-admin-registration-form-page/',admin_reg_form),
    path('e-com-admin-login-form-page/',admin_login),

]