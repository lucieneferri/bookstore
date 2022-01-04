from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from core.models import Batch, Books, Authors, Client, Order,Usuario

admin.site.register(Batch)
admin.site.register(Books)
admin.site.register(Authors)
admin.site.register(Client)
admin.site.register(Order)
admin.site.register(Usuario, UserAdmin)

