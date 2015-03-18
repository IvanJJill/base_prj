from django.contrib import admin
from bicycles.models import Bicycle
from bicycles.models import Client
from bicycles.models import Order

admin.site.register(Bicycle)
admin.site.register(Client)
admin.site.register(Order)
# Register your models here.
