from django.contrib import admin

from core.models import Authors, Batch, Books, Client, Order

admin.site.register(Batch)
admin.site.register(Books)
admin.site.register(Authors)
admin.site.register(Client)
admin.site.register(Order)

