from django.db import models

# Create your models here.
class ecom_seller_register_datatable(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=20)
    uname=models.CharField(max_length=20)
    email=models.EmailField()
    phone=models.IntegerField()
    gender=models.CharField(max_length=10)
    # dob=models.DateField()
    address=models.CharField(max_length=100)
    pw=models.CharField(max_length=15)
    imgfile =models.ImageField(upload_to='ecom_app/static')
    def __str__(self):
        return self.uname

class ecomsellerproductupload(models.Model):
    prod_name = models.CharField(max_length=50)
    imgfile = models.FileField(upload_to='ecom_app/static')
    prod_category = models.CharField(max_length=40)
    prod_size = models.CharField(max_length=10)
    prod_price = models.IntegerField()
    prod_details = models.CharField(max_length=1000)
    login_id = models.IntegerField()
    def __str__(self):
        return self.prod_category

class ecom_buyer_register_datatable(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=20)
    uname = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.IntegerField()
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    pw = models.CharField(max_length=15)
    def __str__(self):
        return self.email
class ecom_buyer_wishlist_datatable(models.Model):
    user_loginid = models.IntegerField()
    prod_id = models.IntegerField()
    prod_name = models.CharField(max_length=50)
    imgfile = models.FileField()
    prod_category = models.CharField(max_length=40)
    prod_size = models.CharField(max_length=10)
    prod_price = models.IntegerField()
    prod_details = models.CharField(max_length=1000)

class ecom_buyer_cart_datatable(models.Model):
    user_loginid = models.IntegerField()
    prod_id = models.IntegerField()
    prod_name = models.CharField(max_length=50)
    imgfile = models.FileField()
    prod_category = models.CharField(max_length=40)
    prod_size = models.CharField(max_length=10)
    prod_price = models.IntegerField()
    prod_details = models.CharField(max_length=1000)
    prod_quantity = models.IntegerField()

class buyer_address_datatable(models.Model):
    fullname = models.CharField(max_length=40)
    addressline1 = models.CharField(max_length=70)
    addressline2 = models.CharField(max_length=70)
    street = models.CharField(max_length=30)
    phone = models.IntegerField()
    pin = models.CharField(max_length=10)
    user_loginid = models.IntegerField()

class user_final_confirm_details_table(models.Model):
    user_loginid = models.IntegerField()
    uname = models.CharField(max_length=20)
    delivery_address = models.CharField(max_length=100)
    order_items = models.CharField(max_length=300)
    amount_paid = models.IntegerField()
    order_date = models.DateField(auto_now_add=True)
    est_delivery_date = models.DateField()

class My_Orders(models.Model):
    user_loginid = models.IntegerField()
    prod_id_list = models.JSONField()
    order_date = models.DateField()