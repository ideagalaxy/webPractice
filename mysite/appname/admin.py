from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)

admin.site.register(User)
admin.site.register(Person)
admin.site.register(BankBook)