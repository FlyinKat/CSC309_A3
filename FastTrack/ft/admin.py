from django.contrib import admin
from .models import User
from .models import Listing
from .models import Rating

# Register your models here.

admin.site.register(User)
admin.site.register(Listing)
admin.site.register(Rating)