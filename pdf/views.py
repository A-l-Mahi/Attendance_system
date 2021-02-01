from django.shortcuts import render

import datetime

from mainP.models import save
# Create your views here.
from django.http import HttpResponse

from django.views.generic import  View      

from django.template.loader import get_template

from .utils import render_to_pdf



class generate(View):
    def get(self, request, *args, **kwargs):
        template = get_template('tables.html')

        context = {
             
            "info" : save.objects.all(),
            
            "Date": datetime.datetime.today(),   

        }
        html = template.render(context)
        pdf = render_to_pdf('tables.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Attendance_Sheet%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")
