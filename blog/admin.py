from django.contrib import admin

from . import models


admin.site.register(models.Topic)
admin.site.register(models.Post)
admin.site.register(models.About)
admin.site.register(models.Contact)
admin.site.register(models.Info)
