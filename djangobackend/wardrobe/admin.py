from django.contrib import admin
from .models import Clothing

# Register your models here.


class ClothingModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'description')
    list_per_page = 10


admin.site.register(Clothing, ClothingModelAdmin)
