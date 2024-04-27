from django.contrib import admin

from users.models import User

# Register your models here.


# admin.site.register(User)


@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', "last_name")
    search_fields = ('username', 'first_name', 'last_name', 'email')
