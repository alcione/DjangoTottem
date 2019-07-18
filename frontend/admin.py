from django.contrib import admin
from .models import Category, SubCategory, SubCategoryItem


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display  = ('id','name', 'image', 'status', 'created_at', 'updated_at')
    search_fields = ['name']
    #prepopulated_fields = {"slug": ("name",)}

class SubCategoryAdmin(admin.ModelAdmin):
    list_display  = ('id','name', 'sigla', 'status', 'created_at', 'updated_at')
    search_fields = ['sigla']


class SubCategoryItemAdmin(admin.ModelAdmin):
    list_display  = ('id','title', 'subcategory', 'link', 'status', 'created_at', 'updated_at')
    search_fields = ['title']

admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(SubCategoryItem, SubCategoryItemAdmin)