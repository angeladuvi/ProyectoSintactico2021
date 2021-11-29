from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def principal(request):
    template_name='sintactico/sintactico.html'
    diccionariocontexto = {'lista' :[1,2,3,4,5]}
    return render(request, template_name,diccionariocontexto)


#def principal(request):
#   return HttpResponse('<h1>Sintactico Estructural</h1>')