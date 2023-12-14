from django.contrib import admin
from products.models import *


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at"]
    list_filter = ["created_at", "updated_at"]
    search_fields = ["title"]


@admin.register(ColorModel)
class ColorModelAdmin(admin.ModelAdmin):
    list_display = ["title", "code", "created_at"]
    list_filter = ["created_at", "updated_at"]
    search_fields = ["title", "code"]


@admin.register(TagModel)
class TagModelAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at"]
    list_filter = ["created_at", "updated_at"]
    search_fields = ["title"]


@admin.register(CompanyModel)
class CompanyModelAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at"]
    list_filter = ["created_at", "updated_at"]
    search_fields = ["title"]


@admin.register(ProductModel)
class ProductsModelAdmin(admin.ModelAdmin):
    list_display = ["title", "price", "created_at"]
    list_filter = ["created_at", "updated_at"]
    search_fields = ["title", "short_description"]


