from django.contrib import admin

# Register your models here.
from .models import tables,productlist,subscribe,getID,contact_form,shoping_cart1
admin.site.register(tables)
admin.site.register(getID)
admin.site.register(productlist)
admin.site.register(contact_form)
admin.site.register(subscribe)
admin.site.register(shoping_cart1)