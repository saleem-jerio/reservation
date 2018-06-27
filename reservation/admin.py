# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Hotel, Customer, Reservation

admin.site.register(Hotel)
admin.site.register(Customer)
admin.site.register(Reservation)