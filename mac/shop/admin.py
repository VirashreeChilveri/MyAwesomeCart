from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product,Contact,Orders,OrderUpdate,Cart
admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(OrderUpdate)
admin.site.register(Cart)

admin.site.site_header='MyAwesomeCart'
admin.site.index_title = 'Features area'
admin.site.site_title='MyAwesomeCart'


