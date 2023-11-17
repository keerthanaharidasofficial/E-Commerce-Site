from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(ecom_seller_register_datatable)
admin.site.register(ecomsellerproductupload)
admin.site.register(ecom_buyer_register_datatable)