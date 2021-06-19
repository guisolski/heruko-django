from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def index(request):

    #data_atual = date.today()
    #return HttpResponse(data_atual)
    return render(request, "index.html")

def page2(request):

    return render(request, "page2.html")

def page3(request):

    html = '''
    <html>
        <head><title>Página 3</title></head>
        <body>
            <h1>Python no Heroku - SOCPS</h1>
            <h2>Página 3</h2>
            <a href="../">index</a>
            <a href="{% url 'page4' %}">pagina 4</a>
        </body>
    </html>
    '''
    return HttpResponse(html)

def page4(request):
    return render(request,"page4.html")

def page5(request):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    html = '''
        <html>
            <head><title>Página 5</title></head>
            <body>
                <h1>{date}</h1>
            </body>
        </html>
        <a href="{% url 'page2' %}">Página 2</a>
        <a href="{% url 'page4' %}">Página 4</a>
    '''.format(date=dt_string)
    return HttpResponse(html)
