from django.db import models
from users.models import User


class Event(models.Model):
    title = models.TextField(blank=False)
    description = models.TextField(blank=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    # begin_at = models.DateField(blank=True)
    # end_at = models.DateField(blank=False)
    # max_users = models.IntegerField(blank=False)
    # is_active = models.BooleanField(blank=False, default=False)

    class Meta:
        db_table = 'events'
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def __str__(self):
        return f'{self.id}, title ({self.title}), description ({self.description})'


class EventsUser(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    event_id = models.OneToOneField(Event, on_delete=models.CASCADE)
    created_at = models.DateField(blank=False)
    score = models.IntegerField()

    class Meta:
        db_table = 'events_users'
        verbose_name = 'Event user'
        verbose_name_plural = 'Events users'

    def __str__(self):
        return f'{self.id}, user_id ({self.user_id}), event_id ({self.event_id})'
