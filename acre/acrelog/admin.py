from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(event)
admin.site.register(operation)
admin.site.register(location)
admin.site.register(operator)
admin.site.register(seed)
admin.site.register(fertilizer)
admin.site.register(log)
# admin.site.register(ModelName)