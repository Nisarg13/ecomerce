from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Product)
admin.site.register(ProductManager)
admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(tbl_User)
