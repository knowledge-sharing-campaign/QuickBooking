from django.db import models
from django.utils import timezone

class Passenger(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    Phone = models.IntegerField()

class BusType(models.Model):
    type = models.CharField(primary_key=True, max_length=20)

    def __unicode__(self):
        return self.type

class Bus(models.Model):
    company = models.CharField(max_length=200)
    make = models.CharField(max_length=100)
    capacity = models.IntegerField(default=50)
    type = models.ForeignKey(BusType)

    def __unicode__(self):
        return "%s %s" % (self.company, self.make)

class BusStop(models.Model):
    stopname = models.CharField(primary_key=True, max_length=100)

    def __unicode__(self):
        return self.stopname

class Timing(models.Model):
    depart = models.DateTimeField(default=timezone.now, blank=True)
    arrival = models.DateTimeField(default=timezone.now, blank=True)

    def __unicode__(self):
        return "depart: %s arival: %s" % (str(self.depart), str(self.arrival))

class BusRoute(models.Model):
    src = models.ForeignKey(BusStop, related_name="source")
    dest = models.ForeignKey(BusStop, related_name="destination")
    bus = models.ForeignKey(Bus)
    timing = models.ForeignKey(Timing)
    cost = models.IntegerField(default=1000)

    def __unicode__(self):
        return "%s -> %s >>> %s" % (self.src, self.dest, self.bus)
    