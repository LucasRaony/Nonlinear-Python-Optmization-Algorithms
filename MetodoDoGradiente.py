import math
from numpy import *

def f(xk):
    return xk[0][0]**2 + xk[1][0]**2
def f2(xk):
    return xk[0][0]**2 + xk[1][0]**2 - 8*xk[0][0] + 5*xk[1][0] + 22.25
def f3(xk):
    return 9*(xk[0][0]**2) - 3*xk[0][0]*xk[1][0] + 1.25*(xk[1][0]**2) - 24*xk[0][0] + 9*xk[1][0] + 22.25
def f4(xk):
    return 0.5*(xk[0][0]**2) + 0.25*(xk[1][0]**2) + 20*math.sin(0.1*xk[0][0]*xk[1][0]) + 0.25
#-------------------------------------------------------------------------------
def calcGradiente(xk):
    return array([    [2*xk[0][0]],
                      [2*xk[1][0]]])
def calcGradiente2(xk):
    return array([    [(2*xk[0][0])-8],
                      [(2*xk[1][0])+5]])
def calcGradiente3(xk):
    return array([    [(18 *xk[0][0]) - (3*xk[1][0]) - 24],
                      [(2.5*xk[1][0]) - (3*xk[0][0]) + 9 ]])
def calcGradiente4(xk):
    return array([    [    xk[0][0] + 2*xk[1][0]*math.cos(0.1*xk[0][0]*xk[1][0])],
                      [0.5*xk[1][0] + 2*xk[0][0]*math.cos(0.1*xk[0][0]*xk[1][0])]])
#-------------------------------------------------------------------------------

def MetodoDoGradiente():
    t = 1.0; n = 0.25; gama = 0.8; ERRO = 0.000001; armijo = False; i = 0;
    xk = array([[0],
                [0]])
    
    print("Ponto Inicial:\n"                       ,xk                )
    print("Gradiente da função no ponto inicial:\n",calcGradiente2(xk))#MUDA
    d = 0
    while(dot(calcGradiente2(xk).transpose(),calcGradiente2(xk))>ERRO ):#MUDA
        d = -calcGradiente2(xk)#MUDA
        while( f2(xk+t*d) >  f2(xk) + t * n * dot(calcGradiente2(xk).transpose(), d) ):#MUDA
            t = t * gama;
            armijo = True
        xk = xk + t*d
        i += 1
    if armijo == True: print("----Entrou no armijo----")
    print("Ponto final:\n"                       ,xk                )
    print("Gradiente da função no ponto final:\n",calcGradiente2(xk))#MUDA
    print("Direção de descida final:\n"          ,d                 )              
    print("Número de iterações:"                 ,i                 )

MetodoDoGradiente()

