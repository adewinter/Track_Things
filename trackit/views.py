from datetime import datetime
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseForbidden, HttpResponse
from django.template import RequestContext
from django.core.management import call_command
from trackit.models import Chart, DataPoint

def show_charts(request, userid=None, time_start=None, time_end=None):
    context = {}
    if not userid:
        charts = Chart.objects.all()
    else:
        charts = Chart.objects.filter(user__id=userid)

    time_start = request.GET.get("time_start", None)
    charts_info = []
    for chart in charts:
        charts_info.append(get_chart_dict(chart, time_start, time_end))

    context["charts_bundle"] = charts_info
    return render_to_response("trackit/show_charts.html", context, context_instance=RequestContext(request))

def get_chart_dict(chart, time_start=None, time_end=None):
    """
    Given a chart and a time_range, returns a convenient dict
    containing information to make chart rendering easier.
    """
    if not time_end:
        time_end = datetime.now()

    if not time_start:
        data_points = DataPoint.objects.filter(chart=chart, created_on__lte=time_end)
    else:
        data_points = DataPoint.objects.filter(chart=chart, created_on__lte=time_end, created_on__gte=time_start)

    data_points.order_by('-created_on')
    c = {}
    c["chart"] = chart
    data = []
    for pt in data_points:
        data.append([pt.quantity, pt.created_on])

    c["data"] = data
    return c