from django.db import models

# Create your models here.
class Weather(models.Model):
    temp = models.CharField(max_length=5)
    humidity = models.CharField(max_length=5)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.temp