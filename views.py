#i have created this file-niki
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.GET.get('text','default')
    print(djtext)
    return HttpResponse("remove punc <a href='/''>back</a>")
#def ex1(request):
#    s='''<h2>Navigation Bar <br> </h2>
#    <a href="https://www.amazon.in/"> amazon </a> <br>
#    <a href="https://web.whatsapp.com/"> What's up </a> <br>
#    <a href="https://www.ajio.com"> Ajio </a> <br>
#    <a href="https://stackoverflow.com/"> stackoverflow </a>'''
#    return HttpResponse(s)

#def about(request):
#    return HttpResponse("About hello niki")



#def capfirst(request):
#        return HttpResponse("capitalize first <a href='/'>back</a>")

#def newlineremove(request):
#        return HttpResponse("newline remove first <a href='/'>back</a>")

#def spaceremove(request):
#   return HttpResponse("space remove back <a href='/'>back</a>")

#def charcount(request):
#       return HttpResponse("charcount <a href='/'>back</a>")
