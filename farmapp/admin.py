from django.contrib import admin
from farmapp.models import Member, Products, ImageModel, Order, Contact, Subscriber, Blog_single, Appointment

# Register your models here.
admin.site.register(Member)
admin.site.register(Products)
admin.site.register(ImageModel)
admin.site.register(Order)
admin.site.register(Contact)
admin.site.register(Blog_single)
admin.site.register(Subscriber)
admin.site.register(Appointment)
