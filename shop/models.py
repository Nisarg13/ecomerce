from django.db import models
import datetime
from datetime import datetime


# Create your models here.
class tbl_User(models.Model):
    email=models.EmailField(unique=True )
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    confirmpassword=models.CharField(max_length=20)
    otp=models.IntegerField(default=459)
    is_active=models.BooleanField(default=False,blank=True)
    is_verfied=models.BooleanField(default=False,blank=True)
    role=models.CharField(max_length=30)
    created_at=models.DateTimeField(auto_now_add=True,blank=False)
    updated_at=models.DateTimeField(auto_now=True,blank=False)
    terms=models.BooleanField(default=False,blank=True)



class ProductManager(models.Model):
    user_id=models.ForeignKey(tbl_User,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=20,blank=True)
    companyname=models.CharField(max_length=20,blank=True)
    companylogo=models.FileField(upload_to="shop/images",default="boy.png",blank=True)
    contactno=models.CharField(max_length=20,blank=True)
    address=models.CharField(max_length=20,blank=True)
    website=models.CharField(max_length=50,blank=True)

class Customer(models.Model):
    user_id=models.ForeignKey(tbl_User,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=20,blank=True)
    contactno=models.CharField(max_length=20,blank=True)

class Category(models.Model):
    cname=models.CharField(max_length=30)


class color_tbl(models.Model):
    select_color=models.CharField(max_length=20)

    def __str__(self):
        return self.select_color

class Product(models.Model):
    user_id=models.ForeignKey(tbl_User,on_delete=models.CASCADE)
    pid=models.ForeignKey(ProductManager,on_delete=models.CASCADE)
    cid=models.ForeignKey(Category,on_delete=models.CASCADE)
    color=models.ManyToManyField(color_tbl)
    product_id=models.AutoField
    produt_name=models.CharField(max_length=50)
    category=models.CharField(max_length=50,default="")
    subcategory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=300)
    pub_date=models.DateField()
    image=models.ImageField(upload_to="shop/images",default="")
    def __str__(self):
        return self.produt_name
    def color_list(self):
        return [str(color)for color in self.color.all()]


class cart(models.Model):
    #user_id=models.ForeignKey(tbl_User,on_delete=models.CASCADE)
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    c_id=models.ForeignKey(Customer,on_delete=models.CASCADE)
    qty=models.IntegerField(default=0)
    #total=models.IntegerField(default=0)
    def price(self):
        return self.qty * self.product_id.price

class wishlist_tbl(models.Model):
    c_id=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    qty=models.IntegerField(default=0)

class Address(models.Model):
    c_id=models.ForeignKey(Customer,on_delete=models.CASCADE)
    name=models.CharField(max_length=50,blank=True)
    address_line1=models.CharField(max_length=200,blank=True)
    address_line2=models.CharField(max_length=200,blank=True)
    city=models.CharField(max_length=200,blank=True)
    country=models.CharField(max_length=200,blank=True)
    zip_code=models.CharField(max_length=200,blank=True)
    contact_no=models.CharField(max_length=200,blank=True)

    
class order(models.Model):
    c_id=models.ForeignKey(Customer,on_delete=models.CASCADE)
    order_date=models.DateTimeField(auto_now_add=True)
    address=models.ForeignKey(Address,on_delete=models.CASCADE)
    status=models.CharField(max_length=20,choices=(
        ('Ordered','Ordered'),('Shipped','Shipped'),('Dispatched','Dispatched'),('Delivered','Delivered')
    ))

class order_item(models.Model):
    order=models.ForeignKey(order,on_delete=models.CASCADE)
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    qty=models.IntegerField(default=0)
    price=models.IntegerField(default=1)

class payment(models.Model):
    order=models.ForeignKey(order,on_delete=models.CASCADE)
    payment_method=models.CharField(max_length=50,choices=(
        ("Card","Card"),("PayPal","PayPal")
    ))
    successfull=models.BooleanField(default=False)
    amount=models.FloatField()
    payment_date=models.DateTimeField(auto_now_add=True)

