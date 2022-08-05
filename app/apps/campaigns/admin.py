from django.contrib import admin
from .models import (
    Campaign,
    Brand,
    Interest,
    Category,
)

admin.site.register(Campaign)
admin.site.register(Brand)
admin.site.register(Interest)
admin.site.register(Category)