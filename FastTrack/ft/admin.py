from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Customer)
admin.site.register(Courier)
admin.site.register(Rating)
admin.site.register(CustomerListing)
admin.site.register(CourierListing)