from django.contrib import admin
from .models import Informativos
# Register your models here.
@admin.register(Informativos)
class InformativoAdmin(admin.ModelAdmin):
    pass