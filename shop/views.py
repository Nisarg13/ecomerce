from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from math import ceil
from django.db.models import Avg, Max, Min, Sum
from django.urls import reverse     
from django.conf import settings
from django.views.decorators.cache import cache_control
import stripe
# Create your views here.

stripe.api_key = "<YOUR STRIPE API KEY>"

def index(request):
    data=Product.objects.all()
    if "email" in request.session:
        #w_data=wishlist_tbl.objects.filter(c_id_id=request.session['cid'])
        #request.session['wishlist_length']=len(w_data)
        uid=tbl_User.objects.get(email=request.session['email'])
        return render(request,"shop/index.html",{'uid':uid})
    else:
        return render(request,'shop/index.html',{'data':data})



def about(request):
    return render(request,'shop/about.html')



def loginpage(request):
    if "email" in request.session:
        return HttpResponseRedirect(reverse(index))
    else:
        return render(request,"shop/login.html")



def login(request):
    if "email" in request.session:
            return HttpResponseRedirect(reverse(index))
    else:
        try:
            u_email=request.POST['email']
            u_password=request.POST['password']
            u_role=request.POST['role']
            uid=tbl_User.objects.filter(email=u_email,role=u_role)
            print("--------------->616161")
            cid=Customer.objects.filter(user_id=uid[0])
            w_data=wishlist_tbl.objects.filter(c_id=cid[0])
            print("--------------->2151")
            if uid:
                if uid[0].password==u_password:
                    if uid[0].role==u_role:
                        print("------->Hello ",uid[0].username)
                        print("------->Role: ",uid[0].role)
                        request.session['username']=uid[0].username
                        request.session['email']=uid[0].email
                        request.session['cid']=cid[0].id
                        request.session['wishlist_length']=len(w_data)
                        print("------------->wishlist:",request.session['wishlist_length'])
                        print("---------------------->",cid[0].id)
                        return HttpResponseRedirect(reverse(index))
                    else:
                        print("------------------>else")
                        return HttpResponseRedirect(reverse('loginpage'))
                else:
                    print("------------------>else")
                    return HttpResponseRedirect(reverse('loginpage'))
            else:
                e_msg="Invalid email address or password"
                return render(request,"shop/login.html",{'e_msg':e_msg})
        except Exception as e:
                e_msg="Enter email address and password"
                print("---------------------->",e)
                return render(request,"shop/login.html",{'e_msg':e_msg})



def logout(request):
    try:
        if "email" in request.session:
            request.session.flush()
            return HttpResponseRedirect(reverse('loginpage'))
        else:
            return render(request,"shop/login.html")
    except:
        return HttpResponseRedirect(reverse('loginpage'))



def registrationpage(request):
    if "email" in request.session:
        return HttpResponseRedirect(reverse(index))
    else:
        return render(request,"shop/registration.html")



def register(request):
    try:
        u_name=request.POST['username']
        u_password=request.POST['password']
        u_email=request.POST['email']
        u_role=request.POST['role']
        u_contactnumber=request.POST['contactno']
        print(u_role)
        if u_role=="Product Manager":
            uid=tbl_User.objects.create(email=u_email,password=u_password,username=u_name,role=u_role)
            pid=ProductManager.objects.create(user_id=uid,contactno=u_contactnumber)
            if pid:
                print("Successfully Register")
                msg="Successfully register"
                return render(request,"shop/registration.html",{'smsg':msg})
            else:
                print("Error")
                msg="Invalid email and password"
                return render(request,"shop/registration.html",{'emsg':msg})
        else:
            uid=tbl_User.objects.create(email=u_email,password=u_password,username=u_name,role=u_role)
            cid=Customer.objects.create(user_id=uid,contactno=u_contactnumber)
            if cid:
                print("Successfully Register")
                msg="Successfully register"
                return render(request,"shop/registration.html",{'smsg':msg})
            else:
                print("Error")
                msg="Invalid email and password"
                return render(request,"shop/registration.html",{'emsg':msg})
    except Exception as e:
        print(e)
        msg="Already exist"
        return render(request,"shop/registration.html",{'emsg':msg})


        
def rab_shop_left_sidebar_grid(request):
    data=Product.objects.all()
    w_data=wishlist_tbl.objects.filter(c_id_id=request.session['cid'])
    request.session['wishlist_length']=len(w_data)
    return render(request,"shop/05-rab-shop-left-sidebar-grid.html",{'data':data})



def classic(request):
    return render(request,"shop/classic.html")



def view_cart(request):
    if "email" not in request.session:
        return HttpResponseRedirect(reverse(index))
    else:
        c_data=cart.objects.filter(c_id_id=request.session['cid'])
        my_total=0
        for i in c_data:
            my_total+=i.price()
        total_price=my_total+30
        print("------------------>total_price",my_total)
        w_data=wishlist_tbl.objects.filter(c_id_id=request.session['cid'])
        request.session['wishlist_length']=len(w_data)
        return render(request,"shop/11-rab-shop-cart.html",{'c_data':c_data,'my_total':my_total,'total_price':total_price})



def add_cart(request,pk):
    try:
        if "email" not in request.session:
            return HttpResponseRedirect(reverse(index))
        else:
            print("-------------------------->",pk)
            p_id=Product.objects.get(id=pk)
            cid=cart.objects.filter(product_id=p_id,c_id_id=request.session['cid'])
            wid=wishlist_tbl.objects.filter(product_id=p_id,c_id=cid)
            c_data=cart.objects.filter(c_id_id=request.session['cid'])
            #total=cid[0].total
            #total_price=cart.objects.all().aggregate(Sum('price'))
            #print("------------------>total_price",total_price)
        # price=Product.objects.get(price=price)
            if cid:
                cid=cart.objects.get(product_id=p_id,c_id_id=request.session['cid'])
                c_data=cart.objects.filter(c_id_id=request.session['cid'])
                my_total=0
                qty=cid.qty+1
                cid.qty=qty
                cid.save()
                for i in data:
                    my_total+=i.price()
                total_price=my_total+30
                print("---------------------->qty",qty)
                
                #cid.total=total
                print("---------------------->qty",qty)
                print("------------------------------->",my_total)
                c_data=cart.objects.filter(c_id_id=request.session['cid'])
                w_data=wishlist_tbl.objects.filter(c_id_id=request.session['cid'])
                request.session['wishlist_length']=len(w_data)
                return render(request,"shop/11-rab-shop-cart.html",{'c_data':c_data,'my_total':my_total,'total_price':total_price})
            else:
                cart_insert=cart.objects.create(product_id=p_id,qty=1,c_id_id=request.session['cid'])
                total=0
                #data=cart.objects.all()
                my_total=0
                for i in data:
                    my_total+=i.price()
                total_price=my_total+30
                print("-------------------------->",my_total)
                #cid.save()
                c_data=cart.objects.filter(c_id_id=request.session['cid'])
                w_data=wishlist_tbl.objects.filter(c_id_id=request.session['cid'])
                request.session['wishlist_length']=len(w_data)
                return render(request,"shop/11-rab-shop-cart.html",{'c_data':c_data,'my_total':my_total,'total_price':total_price})

    except:
        return HttpResponseRedirect(reverse(wishlist))


def wishlist(request):
    if "email" not in request.session:
        return HttpResponseRedirect(reverse(index))
    else:
        w_data=wishlist_tbl.objects.filter(c_id_id=request.session['cid'])
        request.session['wishlist_length']=len(w_data)
        return render(request,"shop/wishlist.html",{'w_data':w_data})


def add_wishlist(request,pk):
    if "email" not in request.session:
        return HttpResponseRedirect(reverse(index))
    else:
        print("-------------------------->",pk)
        p_id=Product.objects.get(id=pk)
        wid=wishlist_tbl.objects.filter(product_id=p_id,c_id_id=request.session['cid'])
        if wid:
            pass
        else:
            wish_insert=wishlist_tbl.objects.create(product_id=p_id,qty=1,c_id_id=request.session['cid'])
            
        return HttpResponseRedirect(reverse("wishlist"))
def remove_item(request,pk):
    print("-------------------->",pk)
    wid=wishlist_tbl.objects.get(id=pk,c_id_id=request.session['cid'])
    wid.delete()
    w_data=wishlist_tbl.objects.filter(c_id_id=request.session['cid'])
    return render(request,"shop/wishlist.html",{'w_data':w_data})

def remove_item_and_add(request,pk):
    try:
        print("------------------->",pk)
        p_id=Product.objects.get(id=pk)
        c_id=Customer.objects.get(id=request.session['cid'])
        wid=wishlist_tbl.objects.get(product_id=p_id,c_id=c_id)
        cid=cart.objects.filter(product_id=p_id,c_id=c_id)
        c_data=cart.objects.filter(c_id_id=request.session['cid'])
        if cid:
            cid=cart.objects.get(product_id=p_id,c_id=c_id)
            c_data=cart.objects.filter(c_id_id=request.session['cid'])
            my_total=0
            qty=cid.qty+1
            cid.qty=qty
            cid.save()
            for i in c_data:
                my_total+=i.price()
            total_price=my_total+30
            c_data=cart.objects.filter(c_id_id=request.session['cid'])
        else:
            cart_insert=cart.objects.create(product_id=p_id,qty=1,c_id=c_id)
            total=0
            my_total=0
            for i in c_data:
                my_total+=i.price()
                total_price=my_total+30
            c_data=cart.objects.filter(c_id_id=request.session['cid'])
        wid.delete()
        return render(request,"shop/11-rab-shop-cart.html",{'c_data':c_data,'my_total':my_total,'total_price':total_price})
    except:
        return HttpResponseRedirect(reverse(wishlist))


def remove_item_cart(request,pk):
    cid=cart.objects.get(id=pk,c_id_id=request.session['cid'])
    cid.delete()
    c_data=cart.objects.filter(c_id_id=request.session['cid'])
    return render(request,"shop/11-rab-shop-cart.html",{'c_data':c_data})


def incrment_product(request,pk):
    try:
        cid=cart.objects.get(id=pk,c_id_id=request.session['cid'])
        qty=cid.qty+1
        cid.qty=qty
        cid.save()
        return HttpResponseRedirect(reverse(view_cart))
    except:
        return HttpResponseRedirect(reverse(view_cart))


def decrment_product(request,pk):
    try:
        cid=cart.objects.get(id=pk,c_id_id=request.session['cid'])
        qty=cid.qty-1
        cid.qty=qty
        cid.save()
        return HttpResponseRedirect(reverse(view_cart))
    except:
        return HttpResponseRedirect(reverse(view_cart))

def checkout_view(request):
    if "email" not in request.session:
        return HttpResponseRedirect(reverse(index))
    else:
        c_data=cart.objects.filter(c_id_id=request.session['cid'])
        my_total=0
        for i in c_data:
            my_total+=i.price()
        total_price=my_total+30
        print("------------------>total_price",my_total)
        return render(request,"shop/checkout.html",{'c_data':c_data,'my_total':my_total,'total_price':total_price})

def order_complete(request):
    if "email" not in request.session:
        return HttpResponseRedirect(reverse(index))
    else:
        country=request.POST['country']
        print("-------------------------->",country)
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        name=firstname+lastname
        address_line1=request.POST['line1']
        address_line2=request.POST['line2']
        town=request.POST['town']
        state=request.POST['state']
        zip_code=request.POST['zip']
        phoneno=request.POST['phoneno']
        email=request.session['email'],
        amount_in_inr_paisa=int(request.POST['Grand_Total'])*100
        print("-------------------------------->amount:",amount_in_inr_paisa)
        print("--------------------------------->",request.POST['stripeToken'])
        customer=stripe.Customer.create(
        email=request.session['email'],
        name=firstname+lastname,
        source=request.POST["stripeToken"],
        address={
                'line1':address_line1,
                'line2':address_line2,
                'postal_code':zip_code,
                'city':town,
                'state':state,
                'country':country

        }
        )
        print("-------------------------------->",name)
        charge=stripe.Charge.create(
            customer=customer,
            amount=amount_in_inr_paisa,
            currency='inr',
            description='rab_fashion_order',
           # card=source
        
        )
        address=Address.objects.create(c_id_id=request.session['cid'],name=name,address_line1=address_line1,address_line2=address_line2,city=town,country=country,zip_code=zip_code,contact_no=phoneno)
        order_view=order.objects.create(c_id_id=request.session['cid'],status="Ordered",address=address)
        c_id=cart.objects.filter(c_id=request.session['cid'])
        payment.objects.create(order=order_view,amount=(amount_in_inr_paisa/100),payment_method="Card",successfull=True)
        for i in c_id:
            order_item.objects.create(order=order_view,product_id_id=i.product_id_id,qty=i.qty,price=i.product_id.price)
        c_id.delete()
        return render(request,"shop/order_complete.html")