from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Sell)
admin.site.register(Purchase)
admin.site.register(ProductType)
admin.site.register(Product)
admin.site.register(Vendor)
admin.site.register(Department)

