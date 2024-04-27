from django.contrib import admin

from events.models import Event, EventsUser

# Register your models here.


# admin.site.register(User)


@admin.register(Event)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', "description")
    search_fields = ('title', 'description')

@admin.register(EventsUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'event_id', 'created_at', "score")
    search_fields = ('created_at', 'score')