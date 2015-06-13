from django.db import models

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

class BusRoute(models.Model):
    src = models.ForeignKey(BusStop, related_name="source")
    dest = models.ForeignKey(BusStop, related_name="destination")
    bus = models.ForeignKey(Bus)

    def __unicode__(self):
        return "%s -> %s >>> %s" % (self.src, self.dest, self.bus)
