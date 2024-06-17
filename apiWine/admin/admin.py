from django.contrib import admin

from apiWine.models.userModel import User
from ..models.wineModel import Wine

admin.site.register(Wine)
admin.site.register(User)
