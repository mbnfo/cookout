from django.contrib import admin
from .models import Food, Ingredient, Utensil, Profile
# Register your models here.

admin.site.register(Food)
admin.site.register(Ingredient)
admin.site.register(Utensil)
admin.site.register(Profile)