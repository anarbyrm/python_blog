from django.contrib import admin

from . import models


admin.site.register(models.Tag)
admin.site.register(models.Post)
admin.site.register(models.Tutorial)
admin.site.register(models.Lesson)
admin.site.register(models.About)
admin.site.register(models.Contact)
admin.site.register(models.Info)
admin.site.register(models.WebsiteSetting)
