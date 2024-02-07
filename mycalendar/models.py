from django.db import models


class Calendar(models.Model):
    createdBy = models.ForeignKey('auth.User', related_name='calendars', on_delete=models.CASCADE)
    sharedAmong = models.ManyToManyField('auth.User', related_name='shared_calendars')
    timezone = models.CharField(max_length=100)


class Event(models.Model):
    # calendar = models.ForeignKey(Calendar, related_name='events', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    createdBy = models.ForeignKey('auth.User', related_name='events', on_delete=models.CASCADE)
    invites = models.ManyToManyField('auth.User', related_name='invited_events')
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    remindBefore = models.IntegerField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)


