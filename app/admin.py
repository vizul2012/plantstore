from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(seller)
admin.site.register(category)
admin.site.register(product)
admin.site.register(User)
admin.site.register(AddCart)