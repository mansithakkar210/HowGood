# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals
from django.contrib import admin
from django.db import models
from django.db import connection

#class AuthGroup(models.Model):
    #name = models.CharField(unique=True, max_length=80)

    #class Meta:
        #managed = True
        #db_table = 'auth_group'


#class AuthGroupPermissions(models.Model):
    #group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    #permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    #class Meta:
        #managed = True
        #db_table = 'auth_group_permissions'
        #unique_together = (('group', 'permission'),)


#class AuthPermission(models.Model):
    #name = models.CharField(max_length=255)
    #content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    #codename = models.CharField(max_length=100)

    #class Meta:
        #managed = True
        #db_table = 'auth_permission'
        #unique_together = (('content_type', 'codename'),)


#class AuthUser(models.Model):
    #password = models.CharField(max_length=128)
    #last_login = models.DateTimeField(blank=True, null=True)
    #is_superuser = models.BooleanField()
    #username = models.CharField(unique=True, max_length=150)
    #first_name = models.CharField(max_length=30)
    #last_name = models.CharField(max_length=30)
    #email = models.CharField(max_length=254)
    #is_staff = models.BooleanField()
    #is_active = models.BooleanField()
    #date_joined = models.DateTimeField()

    #class Meta:
        #managed = True
        #db_table = 'auth_user'


#class AuthUserGroups(models.Model):
    #user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    #group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    #class Meta:
        #managed = True
        #db_table = 'auth_user_groups'
        #unique_together = (('user', 'group'),)


#class AuthUserUserPermissions(models.Model):
    #user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    #permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    #class Meta:
       # managed = True
        #db_table = 'auth_user_user_permissions'
        #unique_together = (('user', 'permission'),)


class Brand(models.Model):
    c = models.ForeignKey('Company', models.DO_NOTHING)
    name = models.TextField()

    class Meta:
        managed = True
        db_table = 'brand'
        unique_together = (('id', 'id'),)
    def __str__(self):
	  return self.name
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    #list_filter = ('id','master_name',)
    ordering = ('id',)


class Company(models.Model):
    name = models.TextField()
    parent_name = models.TextField(blank=True, null=True)
    employment = models.IntegerField(blank=True, null=True)
    community = models.IntegerField(blank=True, null=True)
    environment = models.IntegerField(blank=True, null=True)
    management = models.IntegerField(blank=True, null=True)
    empowerment = models.IntegerField(blank=True, null=True)
    animal_testing = models.IntegerField(blank=True, null=True)
    renewable_energy = models.IntegerField(blank=True, null=True)
    responsible_ingredients_animal = models.IntegerField(blank=True, null=True)
    responsible_ingredients_mineral = models.IntegerField(blank=True, null=True)
    responsible_ingredients_petro_chem = models.IntegerField(blank=True, null=True)
    class Meta:
       managed = True
       db_table = 'company'
       unique_together = (('id', 'id'),)

class CompanyAdmin(admin.ModelAdmin):
   list_display = ('id','name')
   #list_filter = ('id','master_name',)
   ordering = ('id',)

    


#class DjangoAdminLog(models.Model):
    #action_time = models.DateTimeField()
    #object_id = models.TextField(blank=True, null=True)
    #object_repr = models.CharField(max_length=200)
    #action_flag = models.SmallIntegerField()
    #change_message = models.TextField()
    #content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    #user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    #class Meta:
        #managed = True
        #db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_session'
		
#class ProductIngredientInline(admin.TabularInline):
        #model = ProductIngredient
        #extra = 1

class Ingredient(models.Model):
    master_name = models.TextField()
    scr = models.ForeignKey('LookupSourceCrop', models.DO_NOTHING, blank=True, null=True)
    sl = models.ForeignKey('LookupSourceLabor', models.DO_NOTHING, blank=True, null=True)
    human_safety = models.CharField(max_length=30, blank=True, null=True)
    lp = models.ForeignKey('LookupLciaProxy', models.DO_NOTHING, blank=True, null=True)
    lcia = models.FloatField(blank=True, null=True)
    pubchem_id = models.IntegerField(blank=True, null=True)
    petro = models.NullBooleanField()
    plant_direct = models.NullBooleanField()
    plant_modified = models.NullBooleanField()
    plant_modified_synthetic = models.NullBooleanField()
    mineral = models.NullBooleanField()
    animal = models.NullBooleanField()
    growing_practice = models.TextField(blank=True, null=True)
    ingredient_status = models.TextField(blank=True, null=True)
    #list_display('master_name','animal')

    class Meta:
        managed = True
        db_table = 'ingredient'
		
    def __str__(self):
	  return self.master_name
	
	  
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id','master_name', 'Source_Crop','Source_Labor','petro', 'plant_direct', 'plant_modified', 'mineral', 'animal')
    list_filter = ('petro', 'plant_direct','mineral','animal','scr__name','sl__name')
    search_fields = ('master_name',)
    ordering = ('id',)
    #inlines = (ProductIngredientInline,)
    def Source_Labor(self, obj):
      return obj.sl.name
    def Source_Crop(self, obj):
      return obj.scr
    #def Source_Crop(self, obj):
	  #return obj.petro

class IngredientCasNumber(models.Model):
    i = models.ForeignKey(Ingredient, models.DO_NOTHING)
    cas_number = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ingredient_cas_number'


class IngredientHumanSafetyReference(models.Model):
    hsr = models.ForeignKey('LookupHumanSafetyReference', models.DO_NOTHING, related_name='LookupHumanSafetyReference_hsr')
    i = models.ForeignKey(Ingredient, models.DO_NOTHING)
    name = models.ForeignKey('LookupHumanSafetyReference', models.DO_NOTHING, db_column='name', related_name='LookupHumanSafetyReference_name')
    values = models.TextField(blank=True, null=True)  # This field type is a guess.
    safety_exception = models.NullBooleanField()

    class Meta:
        managed = True
        db_table = 'ingredient_human_safety_reference'


class IngredientSourceCategory(models.Model):
    sc = models.ForeignKey('LookupSourceCategory', models.DO_NOTHING, related_name='LookupSourceCategory_sc')
    i = models.ForeignKey(Ingredient, models.DO_NOTHING)
    name = models.ForeignKey('LookupSourceCategory',models.DO_NOTHING, db_column='name', related_name='LookupSourceCategory_name')

    class Meta:
        managed = True
        db_table = 'ingredient_source_category'


class IngredientSynonym(models.Model):
    i = models.ForeignKey(Ingredient, models.DO_NOTHING)
    master_name = models.TextField()

    class Meta:
        managed = True
        db_table = 'ingredient_synonym'


class LookupCountry(models.Model):
    name = models.CharField(max_length=50)
    score = models.IntegerField()
    sort_order = models.IntegerField()
    active = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'lookup_country'


class LookupGrowingPractice(models.Model):
    name = models.CharField(max_length=50)
    sort_order = models.IntegerField()
    active = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'lookup_growing_practice'
        unique_together = (('id', 'id'), ('name', 'name'),)


class LookupHumanSafety(models.Model):
    name = models.CharField(max_length=50)
    value = models.TextField(blank=True, null=True)
    outcome = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'lookup_human_safety'


class LookupHumanSafetyReference(models.Model):
    name = models.CharField(max_length=50)
    values = models.TextField(blank=True, null=True)  # This field type is a guess.
    sort_order = models.IntegerField()
    active = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'lookup_human_safety_reference'
        unique_together = (('name', 'name'), ('id', 'id'),)


class LookupLciaProxy(models.Model):
    name = models.TextField()
    value = models.FloatField(blank=True, null=True)
    sort_order = models.IntegerField()
    active = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'lookup_lcia_proxy'
        unique_together = (('id', 'id'), ('name', 'name'),)
		
    def __str__(self):
	  return self.name


class LookupPackagingMaterial(models.Model):
    name = models.CharField(max_length=50)
    score = models.IntegerField()
    sortorder = models.IntegerField()
    active = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'lookup_packaging_material'
        unique_together = (('id', 'id'),)


class LookupProcessType(models.Model):
    name = models.CharField(max_length=50)
    score = models.IntegerField()
    sortorder = models.IntegerField()
    active = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'lookup_process_type'
        unique_together = (('id', 'id'),)


class LookupProductStatus(models.Model):
    name = models.CharField(max_length=50)
    sortorder = models.IntegerField()
    active = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'lookup_product_status'
        unique_together = (('id', 'id'),)


class LookupProductType(models.Model):
    name = models.CharField(max_length=100)
    top_type = models.CharField(max_length=50, blank=True, null=True)
    sub_type = models.CharField(max_length=50, blank=True, null=True)
    sub_sub_type = models.CharField(max_length=50, blank=True, null=True)
    sort_order = models.IntegerField()
    active = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'lookup_product_type'
        unique_together = (('id', 'id'),)


class LookupSourceCategory(models.Model):
    name = models.CharField(max_length=50)
    sort_order = models.IntegerField()
    active = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'lookup_source_category'
        unique_together = (('id', 'id'), ('name', 'name'),)


class LookupSourceCrop(models.Model):
    name = models.CharField(unique=True, max_length=50)
    sort_order = models.IntegerField()
    active = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'lookup_source_crop'
		
    def __str__(self):
	  return self.name


class LookupSourceLabor(models.Model):
    name = models.CharField(max_length=50)
    value = models.NullBooleanField()
    sort_order = models.IntegerField()
    active = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'lookup_source_labor'
        unique_together = (('name', 'name'), ('id', 'id'),)
		
    def __str__(self):
	  return self.name


class LookupThresholds(models.Model):
    source_category_percent = models.FloatField(blank=True, null=True)
    source_category = models.FloatField(blank=True, null=True)
    growing_practices_percent = models.FloatField(blank=True, null=True)
    growing_practices = models.FloatField(blank=True, null=True)
    lcia_percent = models.FloatField(blank=True, null=True)
    lcia = models.FloatField(blank=True, null=True)
    number_of_buckets = models.IntegerField(blank=True, null=True)
    weights = models.TextField(blank=True, null=True)  # This field type is a guess.
    active = models.BooleanField()

    class Meta:
        managed = True
        db_table = 'lookup_thresholds'


class Product(models.Model):
    pl = models.ForeignKey('ProductLine', models.DO_NOTHING)
    master_name = models.TextField()
    upc = models.TextField(blank=True, null=True)  # This field type is a guess.
    product_types = models.TextField(blank=True, null=True)  # This field type is a guess.
    local_sourcing = models.NullBooleanField()
    product_rating = models.IntegerField(blank=True, null=True)
    product_status_name = models.CharField(max_length=50, blank=True, null=True)
    ingredient = models.ManyToManyField(Ingredient, through='ProductIngredient')

    class Meta:
        managed = True
        db_table = 'product'
        unique_together = (('id', 'id'),)
    def __str__(self):
	  return self.master_name
	
    #def get_ingredients(self, obj):
	  #return "\n".join([i.ingredients for i in obj.ingredient.all()])
	  
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','master_name', 'Product_Line', 'Brand', 'ingredients')
    list_filter = ('pl__b__name','pl__b__c__name')
    #list_select_related = ('brand',)
    search_fields = ('master_name','pl__name','pl__b__name')
    ordering = ('id',)
    #inlines = (ProductIngredientInline,)
    def Product_Line(self, obj):
	  return obj.pl.name
    def Brand(self, obj):
      return obj.pl.b.name
    def ingredients (self, obj):
      return obj.ingredient.all()
    #def getIngredients(self, obj):
      #cur = connection.cursor()
      #cur.callproc('Product_WinMgr', ['GETNAME',obj.id,cur,])
      #results = cur.fetchall()
      #cur.close()
      #return [Document(*row) for row in results]

class ProductIngredient(models.Model):
    p = models.ForeignKey(Product, models.DO_NOTHING)
    i = models.ForeignKey(Ingredient, models.DO_NOTHING)
    is_field = models.ForeignKey(IngredientSynonym, models.DO_NOTHING, db_column='is_id', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    ingredient_order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'product_ingredient'
        unique_together = (('id', 'id'),)
		
class ProductIngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_id','product', 'ingredient')
    def product_id(self, obj):
       return obj.p.id
    def product(self, obj):
      return obj.p.master_name
    def ingredient(self, obj):
      return obj.i.master_name

class ProductLine(models.Model):
    b = models.ForeignKey(Brand, models.DO_NOTHING)
    name = models.TextField(blank=True, null=True)
    manufacture_location = models.TextField(blank=True, null=True)
    packaging_type = models.TextField(blank=True, null=True)
    processing_type_name = models.TextField(blank=True, null=True)
    product_status_name = models.TextField(blank=True, null=True)
    

    class Meta:
        managed = True
        db_table = 'product_line'
        unique_together = (('id', 'id'),)
		
    def __str__(self):
	  return self.name
	  
class ProductLineAdmin(admin.ModelAdmin):
    list_display = ('name')


class SourceCategoryList(models.Model):
    hg_id = models.IntegerField(blank=True, null=True)
    src_cat_list = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'source_category_list'


class SourceCategoryListNorm(models.Model):
    hg_id = models.IntegerField(blank=True, null=True)
    src_cat = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'source_category_list_norm'


class TtHumanSafety(models.Model):
    p_id = models.IntegerField(blank=True, null=True)
    product_name = models.TextField(blank=True, null=True)
    i_id = models.IntegerField(blank=True, null=True)
    ingredient_name = models.TextField(blank=True, null=True)
    human_safety = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tt_human_safety'


class TtPlantModified(models.Model):
    i_id = models.IntegerField(blank=True, null=True)
    ingredient_name = models.TextField(blank=True, null=True)
    product_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'tt_plant_modified'


class Ttbrand(models.Model):
    id = models.IntegerField(primary_key=True)
    c_id = models.IntegerField()
    name = models.TextField()
    repeat_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ttbrand'


class Ttcompany(models.Model):
    name = models.TextField()
    parent_name = models.TextField(blank=True, null=True)
    employment = models.IntegerField(blank=True, null=True)
    community = models.IntegerField(blank=True, null=True)
    environment = models.IntegerField(blank=True, null=True)
    management = models.IntegerField(blank=True, null=True)
    empowerment = models.IntegerField(blank=True, null=True)
    animal_testing = models.IntegerField(blank=True, null=True)
    renewable_energy = models.IntegerField(blank=True, null=True)
    responsible_ingredients_animal = models.IntegerField(blank=True, null=True)
    responsible_ingredients_mineral = models.IntegerField(blank=True, null=True)
    responsible_ingredients_petro_chem = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ttcompany'


class Ttingredient(models.Model):
    working = models.TextField(blank=True, null=True)
    master_name = models.TextField()
    scr_id = models.IntegerField(blank=True, null=True)
    sl_id = models.IntegerField(blank=True, null=True)
    human_safety = models.NullBooleanField()
    lp_id = models.IntegerField(blank=True, null=True)
    lcia = models.FloatField(blank=True, null=True)
    pubchem_id = models.IntegerField(blank=True, null=True)
    petro = models.NullBooleanField()
    plant_direct = models.NullBooleanField()
    plant_modified = models.NullBooleanField()
    plant_modified_synthetic = models.NullBooleanField()
    mineral = models.NullBooleanField()
    animal = models.NullBooleanField()
    growing_practice = models.TextField(blank=True, null=True)
    ingredient_status = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ttingredient'


class TtingredientSynonym(models.Model):
    working = models.TextField(blank=True, null=True)
    i_id = models.IntegerField()
    master_name = models.TextField()

    class Meta:
        managed = True
        db_table = 'ttingredient_synonym'


class Ttproduct(models.Model):
    pl_id = models.IntegerField()
    master_name = models.TextField()
    upc = models.TextField(blank=True, null=True)
    product_types = models.TextField(blank=True, null=True)
    local_sourcing = models.NullBooleanField()
    product_rating = models.IntegerField(blank=True, null=True)
    product_status_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ttproduct'


class TtproductIngredient(models.Model):
    p_id = models.IntegerField()
    i_id = models.IntegerField()
    is_id = models.IntegerField(blank=True, null=True)
    ingredient_order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ttproduct_ingredient'


class TtproductLine(models.Model):
    b_id = models.IntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    manufacture_location = models.TextField(blank=True, null=True)
    packaging_type = models.TextField(blank=True, null=True)
    processing_type_name = models.TextField(blank=True, null=True)
    product_status_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ttproduct_line'


#class TtproductScore(models.Model):
    #id = models.IntegerField(blank=True, null=True)
    #data = models.TextField(blank=True, null=True)

    #class Meta:
        #managed = True
        #db_table = 'ttproduct_score'
