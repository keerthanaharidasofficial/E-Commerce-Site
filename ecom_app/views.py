# <!---- PROJECT E-COMMERCE WEBSITE------------- Eflyer---------------------
# ------------------------------------GLOBAL VARIABLES USED
# ---------------------------------------1. seller_id : in def my_ecom_login_seller(request):
# ---------------------------------------2. user_loginid
#                                        3. user_uname
#                                        4. total_amount
#                                        5. confirm_del_address_id------------------------------>
import datetime

from django.shortcuts import render,redirect
from django.http import HttpResponse    # to get text response in our web page in accordance with given url request
from .models import *
from datetime import datetime,date, timedelta
from django.core.mail import send_mail
from.forms import *
from django.contrib.auth import authenticate,login
from ecom_project.settings import EMAIL_HOST_USER
# Create your views here.
global uname_list
def my_ecom_index(request):
    request.session['user_loginid'] = 0
    return render(request,'index.html')
def ecom_navbar(request):
    return render(request,'navbar-eflyer.html')
def my_ecom_fashion(request):
    user_uname = request.session.get('user_uname')
    p = ecomsellerproductupload.objects.all()
    imgfile = []
    for i in p:
        img_clone = str(i.imgfile).split('/')[-1]
        imgfile.append(img_clone)
    imgfiles = zip(p,imgfile)
    imgfiles2 = zip(p, imgfile)
    imgfiles3 = zip(p, imgfile)
    return render(request,'fashion.html',{'fashion_prod':imgfiles,'fashion_prod2':imgfiles2,'fashion_prod3':imgfiles3,'username':user_uname})
def my_ecom_jewellery(request):
    user_uname = request.session.get('user_uname')
    p = ecomsellerproductupload.objects.all()
    imgfile = []
    for i in p:
        img_clone = str(i.imgfile).split('/')[-1]
        imgfile.append(img_clone)
    imgfiles = zip(p,imgfile)
    imgfiles2 = zip(p, imgfile)
    imgfiles3 = zip(p, imgfile)
    return render(request,'jewellery.html',{'jewelry_prod':imgfiles,'jewelry_prod2':imgfiles2,'jewelry_prod3':imgfiles3,'username':user_uname})
def my_ecom_login_seller(request):
    if request.method == 'POST':
        uname_login = request.POST.get('uname')
        pw_login = request.POST.get('pw')
        a = ecom_seller_register_datatable.objects.all()  # it is an ORM query that fetch a table from our model field
        for i in a:
            if i.uname == uname_login and i.pw == pw_login:
                request.session['seller_id']=i.id  # to declare global variable..eg.id. can be used anywhere
                # return HttpResponse('Login successfully')
                return redirect(profile_page)
        else:
            return HttpResponse('<center><h1>Login failed<br><h2>Make sure that you enter the details properly'
                                '<br><br>If you are new to Eflyer, Please Register...')
    return render(request,'login_seller.html')
def my_ecom_register_seller(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        address = request.POST.get('address')
        # dob=request.POST.get('dob')
        gender=request.POST.get('gender')
        uname=request.POST.get('uname')
        pw=request.POST.get('pw')
        cpw=request.POST.get('cpw')
        imgfile=request.FILES.get('imgfile')
        a = ecom_seller_register_datatable.objects.all()
        for i in a:
            if i.uname==uname:
                return HttpResponse('Username already exist... Cant register using this username... Try different Username ')
            if i.email==email:
                return HttpResponse('Email already exist...Registration failed... ')
        if pw==cpw:
            a = ecom_seller_register_datatable(fname=fname,lname=lname,email=email,gender=gender,address=address ,phone=phone,imgfile=imgfile,uname=uname,pw=pw)
            a.save()
            return HttpResponse('Registration success')
        else:
            return HttpResponse('Password does not match')
    return render(request,'registration_seller.html')
def ecom_display(request):
    # request.session['seller_id']=None
    r = ecom_seller_register_datatable.objects.all()
    p = ecomsellerproductupload.objects.all()
    w = ecom_buyer_wishlist_datatable.objects.all()
    c = ecom_buyer_cart_datatable.objects.all()
    imgfilenames=[]
    prod_imgfilenames=[]
    wish_imgfilenames = []
    cart_imgfilenames = []

    for i in r:
        imgname_clone = str(i.imgfile).split('/')[-1]
        imgfilenames.append(imgname_clone)      # ['img1.png','img2.png']
        print(imgfilenames)
    for i in p:
        prod_imgname_clone = str(i.imgfile).split('/')[-1]
        prod_imgfilenames.append(prod_imgname_clone)
        print(prod_imgfilenames)
    for i in w:
        wish_imgname_clone = str(i.imgfile).split('/')[-1]
        wish_imgfilenames.append(wish_imgname_clone)
        print(wish_imgfilenames)
    for i in c:
        cart_imgname_clone = str(i.imgfile).split('/')[-1]
        cart_imgfilenames.append(cart_imgname_clone)
        print(cart_imgfilenames)
    file_list = zip(r,imgfilenames)
    prod_file_list = zip(p, prod_imgfilenames)
    wish_file_list = zip(w, wish_imgfilenames)
    cart_file_list = zip(c, cart_imgfilenames)
    print(prod_file_list)
    print(p)
    print(file_list)
    return render(request,'ecom_display.html',{'ecom_seller_reg_key':file_list,'seller_prod_data':prod_file_list,'wishlist':wish_file_list,'cartlist':cart_file_list})
def edit_ecom_seller_register(request,id):
    r = ecom_seller_register_datatable.objects.get(id=id)
    uname_old = r.uname
    if request.method=='POST':
        r.fname = request.POST.get('fname')
        r.lname = request.POST.get('lname')
        r.uname = request.POST.get('uname')
        if uname_old!=r.uname:
            request.session['seller_id']=None
        r.email = request.POST.get('email')
        r.phone = request.POST.get('phone')
        r.address = request.POST.get('address')
        if request.FILES.get('imgfile')==None:
            r.save()
        else:
            r.imgfile = request.FILES.get('imgfile')
        if str(request.POST.get('gender')) in ['male','female']:
            r.gender = request.POST.get('gender')

        r.save()
        return redirect(ecom_display)

    return render(request,'edit_registration_seller.html',{'ecom_seller_data':r})
def edit_ecom_seller_products(request,id):
    p = ecomsellerproductupload.objects.get(id=id)
    if request.method=='POST':

        p.prod_name = request.POST.get('prod_name')
        p.prod_category = request.POST.get('prod_category')
        p.prod_size = request.POST.get('prod_size')
        p.prod_price = request.POST.get('prod_price')
        p.prod_details = request.POST.get('prod_details')
        if request.FILES.get('imgfile')==None:
            p.save()
        else:
            p.imgfile = request.FILES.get('imgfile')
        p.save()
        return redirect(ecom_display)
    return render(request,'edit_seller_products.html',{'seller_prod':p})
def delete_ecom_seller_reg_data(request,id):
    r = ecom_seller_register_datatable.objects.get(id=id)
    r.delete()
    return redirect(ecom_display)
def delete_seller_products(request,id):
    r = ecomsellerproductupload.objects.get(id=id)
    r.delete()
    return redirect(ecom_display)
def ecom_sellerproduct_upload(request,login_id):

    if request.method=='POST':
        # try:

        print('seller login id = ',login_id)
        prod_name = request.POST.get('prod_name')
        imgfile = request.FILES.get('imgfile')
        prod_category = request.POST.get('prod_category')
        prod_size = request.POST.get('prod_size')
        prod_price = request.POST.get('prod_price')
        prod_details = request.POST.get('prod_details')
        p = ecomsellerproductupload(prod_name=prod_name,imgfile=imgfile,prod_category=prod_category,prod_size=prod_size,prod_price=prod_price,prod_details=prod_details,login_id=login_id)
        p.save()
        print('seller uploaded product details successfully')
        return redirect(profile_page)
    # except:
    #     return HttpResponse('Error......Pleaese upload all the Details Correctly')
    return render(request,'ecom_sellerproduct_upload.html')
def profile_page(request):
    try:
        id = request.session['seller_id']
        r = ecom_seller_register_datatable.objects.get(id=id)
        print('login seller :', r.uname)
        imgfile = str(r.imgfile).split('/')[-1]
        print(imgfile)
        return render(request,'profile-page.html',{'seller_profile':r,'imgfile':imgfile})
    except:
        return redirect(my_ecom_login_seller)
def  prod_display_seller(request,id):
    p = ecomsellerproductupload.objects.all()
    prod_imgfilenames = []
    prod_name = []
    prod_details = []
    p1 = []
    for i in p:
        if i.login_id==id:
            p1.append(i)
            prod_imgname_clone = str(i.imgfile).split('/')[-1]
            prod_imgfilenames.append(prod_imgname_clone)
            prod_name.append(i.prod_name)
            prod_details.append(i.prod_details)
            print(prod_imgfilenames)

    prod_list = zip(p1,prod_imgfilenames)
    print(prod_list)

    return render(request, 'display_products.html',{'prod_data':prod_list})
# ---------------------BUYER-------------------------------------------------------------------------------------------
def my_ecom_login_buyer(request):
    if request.method=='POST':
        uname_login = request.POST.get('uname')
        pw_login = request.POST.get('pw')
        r = ecom_buyer_register_datatable.objects.all()
        for i in r:
            if uname_login==i.uname and pw_login==i.pw:
                request.session['user_uname'] = uname_login
                request.session['user_loginid'] = i.id
                return redirect(user_profile_page)
        else:
            return HttpResponse('Login failed... Enter the  Login details')

    return render(request,'login_buyer.html')
def my_ecom_register_buyer(request):
    # uname_list = request.session.get('uname_list')
    if request.method=='POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        uname = request.POST.get('uname')
        # if uname_list!=None:
        #     if uname not in uname_list:
        #         uname_list.append(uname)
        #         request.session['uname_list'] = uname_list
        #         print(uname_list)
        #     else:
        #         return HttpResponse('Username already exist... Cant register register using this username... Try different Username ')
        # else:
        #     uname_list = []
        #     uname_list.append(uname)
        #     request.session['uname_list'] = uname_list
        #     print(uname_list)
        # ----------------------- OR ------------------------------------
        pw = request.POST.get('pw')
        cpw = request.POST.get('cpw')
        a = ecom_buyer_register_datatable.objects.all()
        for i in a:
            if i.uname == uname:
                return HttpResponse('Username already exist... Cant register using this username... Try different Username ')
            if i.email == email:
                return HttpResponse('Email already exist...Registration failed... ')
        if pw==cpw:
            r = ecom_buyer_register_datatable(fname=fname,lname=lname,email=email,phone=phone,address=address,gender=gender,uname=uname,pw=pw)
            r.save()
            return HttpResponse('Buyer Data Successfully added')
        else:
            return HttpResponse('Check your Password...Not Match')
    return render(request,'registration_buyer.html')
def user_profile_page(request):
    user_uname = request.session.get('user_uname')
    if user_uname == None:
        return redirect(my_ecom_index)
    return render(request,'user_profile_page.html',{'username':user_uname})
def user_wishlist_items(request,id):
    print('item id = ',id)
    user_loginid = request.session['user_loginid']
    print('item user login = ',user_loginid )
    p = ecomsellerproductupload.objects.get(id=id)
    w_old = ecom_buyer_wishlist_datatable.objects.all()
    for i in w_old:
        if i.prod_id == id and user_loginid==i.user_loginid:
            return HttpResponse('Item already in wishlist')
    else:
        w = ecom_buyer_wishlist_datatable(user_loginid=user_loginid, prod_id=id, prod_name=p.prod_name,
                                          imgfile=p.imgfile, prod_category=p.prod_category, prod_price=p.prod_price,
                                          prod_size=p.prod_size, prod_details=p.prod_details)
        w.save()
        return redirect(user_profile_page)


def user_wishlist_display(request):
    w =  ecom_buyer_wishlist_datatable.objects.all()
    w1=[]
    wimgfiles = []
    for i in w:
        if i.user_loginid == request.session['user_loginid']:
            w1.append(i)
            img_clone = str(i.imgfile).split('/')[-1]
            wimgfiles.append(img_clone)
    wishlist = zip(w1,wimgfiles)
    print(wishlist)
    return render(request,'wishlist_display.html',{'wishlist_items':wishlist})
def wishlist_item_remove(request,id):
    w = ecom_buyer_wishlist_datatable.objects.get(id=id)
    w.delete()
    return redirect(user_wishlist_display)
def user_logout(request):
    request.session['user_uname'] = None
    request.session['user_loginid'] = 0
    return redirect(my_ecom_index)
from django.contrib.auth import logout
def seller_logout(request):
    request.session['seller_id']=None
    logout(request)
    return redirect(my_ecom_index)
# -----------------------------------CART-----------------------------------------------------------------------------------------------
def user_cart_items(request,id):

    if request.method == 'POST':
        q_c = ecom_buyer_cart_datatable.objects.get(id=id)
        p_p = ecomsellerproductupload.objects.get(id=q_c.prod_id)
        price = p_p.prod_price
        prod_quantity = request.POST.get('prod_quantity')
        if int(prod_quantity) < 1:
            q_c.delete()
            return redirect(user_cart_display)
        else:
            q_c.prod_quantity = prod_quantity
            price *= int(prod_quantity)
            q_c.prod_price = price
            q_c.save()
            return redirect(user_cart_display)
    print('cart item id = ',id)
    prod_quantity = 1
    user_loginid = request.session['user_loginid']
    print('item cart user login = ',user_loginid )
    p_p = ecomsellerproductupload.objects.get(id=id)
    price = p_p.prod_price
    try:
        p = ecomsellerproductupload.objects.get(id=id)
    except:
        p = ecom_buyer_wishlist_datatable.objects.get(id=id)
    c_old = ecom_buyer_cart_datatable.objects.all()
    for i in c_old:
        if i.prod_id == id and user_loginid == i.user_loginid :
            print('item cart user login = ', i.user_loginid)
            print('item cart user login = ', i.prod_id)
            # c = ecom_buyer_cart_datatable.objects.get(prod_id=id)
            i.delete()
            prod_quantity+=1
            price*=prod_quantity
            p.prod_price = price

    else:
        c = ecom_buyer_cart_datatable(user_loginid=user_loginid, prod_id=id, prod_name=p.prod_name,
                                      imgfile=p.imgfile, prod_category=p.prod_category, prod_price=p.prod_price,
                                      prod_size=p.prod_size, prod_details=p.prod_details,prod_quantity=prod_quantity)
        c.save()
        return redirect(user_profile_page)
def user_cart_display(request):

    c =  ecom_buyer_cart_datatable.objects.all()
    print(c)
    c1=[]
    items = ''
    price_total = 0
    cimgfiles = []
    if c:
        user_loginid = request.session['user_loginid']
        print('user login id = ', user_loginid)
        print(c)
        for i in c:
            if i.user_loginid == request.session['user_loginid']:
                price_total += i.prod_price
                c1.append(i)
                items+=(i.prod_category +'-'+i.prod_name+', ')
                img_clone = str(i.imgfile).split('/')[-1]
                cimgfiles.append(img_clone)

        request.session['total_amount'] = price_total
        request.session['cart_item_names'] = items

        if request.session['user_loginid']==0:
            return HttpResponse('<center><br><br><h2>Please Login')

        cartlist = zip(c1,cimgfiles)
        print(cartlist)
        return render(request,'cartlist_display.html',{'cartlist_items':cartlist,'totalprice':price_total,'user_loginid':user_loginid})
    else:
        return HttpResponse('<center><br><br><h2>No Items in the cart')
def cart_item_remove(request,id):
    c = ecom_buyer_cart_datatable.objects.get(id=id)
    c.delete()
    return redirect(user_cart_display)

def proceed_buy_1(request,id):

    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        addressline1 = request.POST.get('addressline1')
        addressline2 = request.POST.get('addressline2')
        street = request.POST.get('street')
        phone = request.POST.get('phone')
        pin = request.POST.get('pin')
        a = buyer_address_datatable(user_loginid=id,fullname=fullname,addressline1=addressline1,addressline2=addressline2,street=street,phone=phone,pin=pin)
        a.save()
        return redirect(f'http://127.0.0.1:8000/ecom_app/e-com-1-buyer-proceed-to-buy-confirm-address-page-2/{id}')
    return render(request,'proceed_buy_page_1.html')
def proceed_buy_2(request,id):
    a_old = buyer_address_datatable.objects.all()
    a = []
    for i in a_old:
        if i.user_loginid == id:
            a.append(i)
    print('all addressess :',a)
    if len(a) == 0:
        return redirect(f'http://127.0.0.1:8000/ecom_app/e-com-1-buyer-proceed-to-buy-items-page-1/{id}')
    else:
        return render(request,'proceed_buy_page_2.html',{'delivery_address':a})
def edit_delivery_address(request,id):
    a = buyer_address_datatable.objects.get(id=id)
    loginid = a.user_loginid
    if request.method=='POST':
        a.fullname = request.POST.get('fullname')
        a.addressline1 = request.POST.get('addressline1')
        a.addressline2 = request.POST.get('addressline2')
        a.street = request.POST.get('street')
        a.phone = request.POST.get('phone')
        a.pin = request.POST.get('pin')
        a.save()
        return redirect(f'http://127.0.0.1:8000/ecom_app/e-com-1-buyer-proceed-to-buy-confirm-address-page-2/{loginid}')

    return render(request,'edit_delivery_address.html',{'address':a})
def delete_delivery_address(request,id):
    r = buyer_address_datatable.objects.get(id=id)
    loginid = r.user_loginid
    r.delete()

    return redirect(f'http://127.0.0.1:8000/ecom_app/e-com-1-buyer-proceed-to-buy-confirm-address-page-2/{loginid}')
def confirm_address_id(request,address_id,loginid):
    request.session['confirm_del_address_id'] = address_id
    print('confirm delivery address id = ',address_id)
    return redirect(f'http://127.0.0.1:8000/ecom_app/e-com-1-buyer-proceed-to-buy-confirm-address-page-2/{loginid}')
def user_payment(request,id):
    request.session['confirm_del_address_id'] = id
    print('confirm delivery address id = ', id)
    if request.method == 'POST':
        c_a = buyer_address_datatable.objects.get(id=id)
        user_loginid = c_a.user_loginid
        uname = c_a.fullname
        amount_paid = request.session['total_amount']
        delivery_address = str(c_a.addressline1)+','+str(c_a.addressline2)
        order_items = request.session['cart_item_names']
        order_date = datetime.today().strftime('%d-%m-%Y')
        est_delivery_date = (datetime.today() + timedelta(days=10)).strftime('%B %d, %Y')
        est_delivery_date= datetime.strptime(est_delivery_date,'%B %d, %Y')
        print(user_loginid,amount_paid,uname,delivery_address,order_items,order_date,est_delivery_date)

        conf = user_final_confirm_details_table(user_loginid=user_loginid,uname=uname,delivery_address=delivery_address,order_items=order_items,
                                                amount_paid=amount_paid,est_delivery_date=est_delivery_date)
        conf.save()
        subject = 'Order Confirmed'
        message = f'Hi {uname}, Your Eflyer Order is confirmed<br> Products will be delivered in 10 days to below address' \
                  '<br>'
        mail_from = 'EMAIL_HOST_USER'
        to_mail = ['keerthana4.rapid@gmail.com']
        send_mail(subject, message, mail_from, to_mail,fail_silently=False)
        return redirect(my_orders)
    return render(request,'payment_user.html')
def my_orders(request):
    # try:
        user_loginid = request.session['user_loginid']
        order_date = date.today()
        c = ecom_buyer_cart_datatable.objects.all()
        prod_id = []
        prod_img = []
        for i in c:
            if user_loginid==i.user_loginid:
                img = str(i.imgfile).split('/')[-1]
                prod_img.append(img)
                prod_id.append(i.prod_id)
                i.delete()

        o = My_Orders(user_loginid=user_loginid,order_date=order_date,prod_id_list=prod_id)
        o.save()
        return render(request, 'my_orders.html',{'imgfiles':prod_img})
    # except:
    #     return HttpResponse('Error.. Order Upload failed')

def my_orders_display(request):
    o = My_Orders.objects.all()
    new_o = []
    final_p = []
    final_imgfile = []
    date = []
    print('length of order items =',len(o))
    if len(o)<=0:
        return HttpResponse('No Order History available')
    else:
        for i in o:
            if i.user_loginid == request.session['user_loginid']:
                new_o.append(i)
                date.append(i.order_date)
                p1 = []
                prod_img = []
                for j in i.prod_id_list:
                    p = ecomsellerproductupload.objects.get(id=j)
                    img = str(p.imgfile).split('/')[-1]
                    prod_img.append(img)
                    p1.append(p)
                # prod_details = zip(prod_img, p1)
                # print('final details zip file = ', prod_details)
                # final_p.append(prod_details)
                final_p.append(p1)
                final_imgfile.append(prod_img)
                final_pp = zip(date,final_p,final_imgfile)
            else:
                return HttpResponse('No Order History available')

        print('final product list in order history :',final_p)
        print('final details in order history :', date)

        return render(request,'my_order_display.html',{'order_date':date,'products':final_pp})
def clear_order_history(request):
    o = My_Orders.objects.all()
    for i in o:
        if i.user_loginid == request.session['user_loginid']:
            i.delete()
    return render(request,'my_order_display.html')
# def send_mail(request):
#     subject = 'Order Confirmed'
#     message = 'Your Eflyer Order is confirmed<br> Products will be delivered in 10 days to below address' \
#               '<br>'
#     mail_from = ''
#     to_mail = 'keerthana4.rapid@gmail.com'
#     send_mail(subject,message,mail_from,to_mail,fail_silently=False)
#     return HttpResponse('Payment details added successfully and your order confirmed <br><br> A confirmation mail has been send to your Email id')


def admin_reg_form(request):
    if request.method=='POST':
        form = AdminRegform(request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            fname = form.cleaned_data['first_name']
            lname = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            pw = form.cleaned_data['password']
            f = User(username=uname,first_name=fname,last_name=lname,email=email)
            f.set_password(pw)
            f.save()
            return HttpResponse('New Admin/ Authenticated User added')
        else:
            return HttpResponse('Data is not valid... User not added')

    form = AdminRegform()
    return render(request,'admin_registration.html',{'form':form})
def admin_login(request):
    if request.method=='POST':
        form = AdminLogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponse('Login successful')
            else:
                return HttpResponse('Username or Password not matches')
        else:
            return HttpResponse('Login failed')
    form = AdminLogin()
    return render(request,'admin_login_form.html',{'form':form})