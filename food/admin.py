from django.contrib import admin
from . import models

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')




admin.site.register(models.Item)


