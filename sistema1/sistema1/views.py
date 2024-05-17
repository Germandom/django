from django.http import HttpResponse
import os
from math import sqrt

def saludo(request):
    return HttpResponse("HOLA MUNDO")

def get_google(request):
    return os.system("Start Chrome")

def get_fibonacci(request):
    
    pos = 100
    lista=[]
    iniFibo = 0
    finFibo = 1

    for x in range(0,pos):
    
        if x == 0:
            finFibo = 0
        elif x == 1:
            finFibo = 1
    
        
        lista.append(f'\nPosicion: {x+1:>4} -- Valor en la serie de Fibonacci:  {finFibo:>10} \n')
    
        sum = finFibo
    
        finFibo = finFibo + iniFibo
        iniFibo = finFibo - iniFibo
    return HttpResponse(lista)

def calculadora(request):
    return os.system('calc')