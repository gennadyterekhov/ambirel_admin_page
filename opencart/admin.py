from django.contrib import admin

from user.models import User
from .models import Category, Product, Attribute, AttributeGroup, Filter, Option


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Attribute)
admin.site.register(AttributeGroup)
admin.site.register(Filter)
admin.site.register(Option)