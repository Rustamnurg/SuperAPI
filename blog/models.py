from django.db import models
from django.utils import timezone


class Report(models.Model):
    device_id = models.BigIntegerField()
    windows_id = models.BigIntegerField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)

#
#     def publish(self):
#         self.published_date = timezone.now()
#         self.save()
#
#     def __str__(self):
#         return self.title
#
#
# class User(models.Model):
#     fistName = models.CharField(max_length=32)
#     lastName = models.CharField(max_length=32)
#     user_id = models.BigIntegerField()
#     bio = models.TextField()
#
#
# class App(models.Model):
#     app_id = models.BigIntegerField()
#     reports = models.ForeignKey()


