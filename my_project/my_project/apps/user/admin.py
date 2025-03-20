from django.contrib import admin
from .models import User
# Register your models here.


# admin.site.register(User)
# admin.site.register(Post)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'is_staff']
    readonly_fields= ['id']

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


