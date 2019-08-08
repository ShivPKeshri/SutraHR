from django.contrib import admin
from .models import CurdOperation

# Register your models here.
class CurdOperationRegister(admin.ModelAdmin):
    list_display = ['id', 'title','created_time', 'updated_time', 'status', 'is_deleted']
    list_display_links = ['id', 'title']

    class Meta:
        model = CurdOperation

admin.site.register(CurdOperation, CurdOperationRegister)