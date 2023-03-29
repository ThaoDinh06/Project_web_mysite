from django.contrib import admin
from firstapp.models import Category, Website, Content


# Register your models here.
# lntri/123456
admin.site.register(Category)
admin.site.register(Website)
admin.site.register(Content)