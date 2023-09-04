from django.contrib import admin

# Register your models here.
from .models import tables,productlist,subscribe,getID
admin.site.register(tables)
admin.site.register(getID)
admin.site.register(productlist)

admin.site.register(subscribe)