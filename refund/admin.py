from django.contrib import admin

# Register your models here.
from .models import Refund

class RefundModel(admin.ModelAdmin):
    list_display = ["name","surname","account","status","updated"]
    list_filter =  ["name", "account"]
    class Meta:
        model = Refund
admin.site.register(Refund, RefundModel)
