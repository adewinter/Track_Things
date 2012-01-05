from django.contrib import admin
from trackit.models import Baseline, Chart, DataPoint

admin.site.register(Chart)
admin.site.register(Baseline)
admin.site.register(DataPoint)
