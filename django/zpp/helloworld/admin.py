from django.contrib import admin
from helloworld.models import User


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    fields = ['name', 'gender', 'desc']
    search_fields = ['name',]
    list_filter = ['name']
    list_display = ['name', 'gender', 'birthday', 'desc']

admin.site.register(User, UserAdmin)
# admin.site.register(User)
