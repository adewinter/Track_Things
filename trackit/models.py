from django.contrib.auth.models import User
from django.db import models
import logging
import os
import urllib
from django.core.files.base import File
import urlparse

logging.getLogger(__name__)

QUANTITY_DESC = "Quantity for this data point, e.g. 5, 11:23pm, \"Happy\" etc"
UNIT_DESC = "The Unit associated with this Data Point, e.g. lbs, kph, inches, etc"
DATAPT_CREATED_ON_DESC = "DateTime this Data Point was created on"
DATAPT_NOTE_DESC = "Additional information to be associated with this data point"

class Baseline(models.Model):
    quantity = models.CharField(max_length=50, help_text=QUANTITY_DESC)
    created_on = models.DateTimeField(auto_now_add=True, help_text=DATAPT_CREATED_ON_DESC)
    description = models.TextField(null=True, blank=True, help_text=DATAPT_NOTE_DESC)
    unit = models.CharField(max_length=255, blank=True, null=True, help_text=UNIT_DESC)

#    def chart(self):
#        return Chart.objects.filter(baseline=self)

    def __unicode__(self):
        return "Baseline Quantity: %s, Units: %s" % (self.quantity, self.unit)

class Chart(models.Model):
    UNITSPAN = (
        ('days', 'Days'),
        ('minutes', 'Minutes'),
        ('hours', 'Hours'),
        ('weeks', 'Weeks'),
        ('months', 'Months'),
        ('years', 'Years')
    )

    name = models.CharField(max_length=255, help_text="The name of this Chart")
    created_on = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now_add=True, auto_now=True)
    description = models.TextField(blank=True, null=True, help_text="Chart Description")
    timespan_units = models.CharField(max_length=50, choices=UNITSPAN, default='days')
    baseline = models.ForeignKey(Baseline)
    user = models.ForeignKey(User)  

    def __unicode__(self):
        return "Chart: %s, last_updated: %s" % (self.name, self.last_updated)

class DataPoint(models.Model):
    quantity = models.CharField(max_length=50, help_text=QUANTITY_DESC)
    created_on = models.DateTimeField(auto_now_add=True, help_text=DATAPT_CREATED_ON_DESC)
    note = models.TextField(null=True, blank=True, help_text=DATAPT_NOTE_DESC)
    unit = models.CharField(max_length=255, blank=True, null=True, help_text=UNIT_DESC)
    chart = models.ForeignKey(Chart)

    def __unicode__(self):
        return "Data Point for Chart: %s :: Quant=%s, Units=%s" % (self.chart, self.quantity, self.unit)

