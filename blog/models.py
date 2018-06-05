from django.db import models
from django.utils import timezone


class User(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    password = models.CharField(max_length=32)


class App(models.Model):
    user = models.ForeignKey(User)
    app_apikey = models.CharField(max_length=64)
    app_name = models.CharField(max_length=32)


class Report(models.Model):
    app = models.ForeignKey(App)
    device_id = models.CharField(max_length=200)
    windows_id = models.CharField(max_length=200)
    message = models.CharField(max_length=200)
    view_name = models.CharField(max_length=200)
    base_rate = models.IntegerField()
    uudid = models.CharField(max_length=200)
    # heatmap_base64
    # app_id
    created_date = models.DateTimeField(
            default=timezone.now)


class View(models.Model):
    report = models.ForeignKey(Report)
    type = models.CharField(max_length=200)
    view_id = models.CharField(max_length=200)
    #  view_image_base64
    coordinates_by_x = models.FloatField()
    coordinates_by_y = models.FloatField()
    message = models.CharField(max_length=200)
    rate = models.IntegerField()
    #  owner


 # author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
 # heatmap_base64


#
#     def publish(self):
#         self.published_date = timezone.now()
#         self.save()
#
#     def __str__(self):
#         return self.title
#
#






