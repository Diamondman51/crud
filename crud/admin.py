from django.contrib import admin

# Register your models here.

admin.site.site_header = "CRUD API Admin"
admin.site.site_title = "CRUD API Admin Portal"
admin.site.index_title = "Welcome to CRUD API Portal"
# admin.site.unregister(admin.models.LogEntry)
from .models import Product, Photo, File
admin.site.register(Product)
admin.site.register(Photo)
admin.site.register(File)
