from django.contrib import admin
from .models import Contact, Update, Picture, Gallery, Bio

# Register your models here.

admin.site.register(Contact)
admin.site.register(Update)
admin.site.register(Picture)
admin.site.register(Gallery)
admin.site.register(Bio)
