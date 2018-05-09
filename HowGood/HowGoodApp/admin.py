# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from HowGoodApp.models import Ingredient, IngredientAdmin
from HowGoodApp.models import Product, ProductAdmin, ProductLine, Brand, BrandAdmin
from HowGoodApp.models import Company, CompanyAdmin
from HowGoodApp.models import ProductIngredient, ProductIngredientAdmin



# Register your models here.
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductLine)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(ProductIngredient, ProductIngredientAdmin)