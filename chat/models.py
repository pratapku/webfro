from django.db import models
class allDevices(models.Model):
    d_id = models.CharField(max_length=40, default=0,primary_key=True)
class Message(models.Model):
    d_id = models.OneToOneField(allDevices, on_delete=models.CASCADE,primary_key=True)
    # username = models.CharField(max_length=255)
    # room = models.CharField(max_length=255)
    sensor1 = models.FloatField(unique = False, max_length=50,default=0.0, blank=True)
    sensor2 = models.FloatField(unique = False, max_length=50,default=0.0, blank=True)
    pin1Status = models.IntegerField(blank=True,null=True,default=0)
    pin2Status = models.IntegerField(blank=True,null=True,default=0)
    
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)