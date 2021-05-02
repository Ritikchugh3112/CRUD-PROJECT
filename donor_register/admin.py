from django.contrib import admin

# Register your models here.
from .models import Donor,Medicalproblem

class MedicalproblemAdmin(admin.ModelAdmin):
    pass
admin.site.register(Medicalproblem,MedicalproblemAdmin)

class DonorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Donor,DonorAdmin)

from django.contrib import admin
# Register your models here.
from .models import Image
admin.site.register(Image)