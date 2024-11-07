from django.db import models
from datetime import datetime


EVENT_TYPES = [
    ('spray', 'Spread/Spray'),
    ('tillage', 'Tillage'),
    ('plant', 'Plant'),
    ('harvest', 'Harvest'),
    ('soil_sampling', 'Soil Sampled')
]



# Create your models here.
class event(models.Model):
    # assign a unique id to each event
    date = models.DateTimeField(default=datetime.now, blank=True)
    event = models.CharField(choices=EVENT_TYPES, max_length=50)
    note = models.TextField()
    def __str__(self):
        return self.date.strftime('%Y-%m-%d') + ' ' + self.event


class operation(models.Model):
    operation = models.CharField(max_length=50)

    def __str__(self):
        return self.operation


class operator(models.Model):
    operator_name = models.CharField(max_length=50)

    def __str__(self):
        return self.operator_name



class location(models.Model):
    location_name = models.CharField(max_length=50)

    def __str__(self):
        return self.location_name



class spray(models.Model):
        powerunit_type = models.CharField(max_length=50)

        def __str__(self):
            return self.powerunit_type



class seed(models.Model):
    seed_planted = models.CharField(max_length=50)
    seed_rate = models.IntegerField()

    def __str__(self):
        return self.seed_planted
    


class fertilizer(models.Model):
    fertilizer_type = models.CharField(max_length=50)
    fertilizer_rate = models.IntegerField()

    def __str__(self):
        return self.fertilizer_type



class log(models.Model):
    location = models.ForeignKey(location, on_delete=models.CASCADE)
    event = models.ForeignKey(event, on_delete=models.CASCADE)
    operator = models.ForeignKey(operator, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now, blank=True)
    note = models.TextField()

    def __str__(self):
        return self.date.strftime('%Y-%m-%d') + ' : ' + self.location.location_name 