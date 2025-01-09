from django.contrib import admin
from . import models


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'updated_at',)
    search_fields = ('name',)
    list_filter = ('created_at', 'updated_at',)

admin.site.register(models.Brand, BrandAdmin)