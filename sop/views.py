from django.http import HttpResponse
from django.conf import settings
import os
from subprocess import run
import sop

pth = os.path.dirname(sop.__file__)

def index(request):
    command = ". ~/.virtualenvs/django2/bin/activate&&"+"python "+os.path.join(settings.BASE_DIR, "manage.py")+" graph_models sop -o "+os.path.join(pth, "static/test2.png")
    print(command)
    print(settings.BASE_DIR)
    status = "Success"
    try:
        run(command, shell=True)
    except Exception as e:
        status = str(e)

    return HttpResponse(("<p>Django, d3.js version</p>",command, status,
        "<p>Class UML graph</p><img src="+os.path.join(pth, "static/test2.png"),"><p>Data table</p><p>Data graph</p>",
        "<p>Choose role</p><p>Return SOPs and training for this role</p>",
        "<p></p><p></p><p></p>"))

