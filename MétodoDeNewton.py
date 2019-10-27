import math
from numpy import *


def f(xk):
    return ( math.exp(xk[0][0]) + math.exp(xk[1][0]) + math.exp(xk[2][0]) + 2 * math.exp(-xk[0][0]-xk[1][0]-xk[2][0]) )
#-----------------------------------------------------------------------------------------------------------------------------------
def calcHessiana(xk):
    aux   = math.exp(-xk[0][0]-xk[1][0]-xk[2][0])
    aux02 = math.exp( xk[0][0]  )
    aux03 = math.exp( xk[1][0]  )
    aux04 = math.exp( xk[2][0]  )
    return array([[aux02+2*aux, 2*aux, 2*aux], [ 2*aux, aux03+2*aux, 2*aux],[ 2*aux, 2*aux, aux04+2*aux]])
#-----------------------------------------------------------------------------------------------------------------------------------
def calcGradiente(xk):
    aux   = math.exp(-xk[0]-xk[1]-xk[2])
    aux02 = math.exp( xk[0][0]  )
    aux03 = math.exp( xk[1][0]  )
    aux04 = math.exp( xk[2][0]  )
    return array([ [(aux02-2*aux)], [(aux03-2*aux)], [(aux04-2*aux)]])
#-----------------------------------------------------------------------------------------------------------------------------------
def MetodoDeNewton():
    t = 1.0; n = 0.25; gama = 0.8; ERRO = 0.000001; armijo = False; i = 0;
    xk = array([[math.log(2)],
                [math.log(2)],
                [math.log(2)]])
    
    print("Ponto Inicial:\n"                       ,xk               )
    print("Gradiente da função no ponto inicial:\n",calcGradiente(xk))
    print("Hessiana da função\n"                   ,calcHessiana (xk))
    
    while(dot(calcGradiente(xk).transpose(),calcGradiente(xk))>ERRO ):
        d = (-1)*(linalg.solve(calcHessiana(xk),calcGradiente(xk)));#encontra 'd' a partir da solução de um sistema Ax=b
        while( f(xk+t*d) >  f(xk) + t * n * dot(calcGradiente(xk).transpose(), d) ):
            t = t * gama
            armijo = True
        xk = xk + t*d;#calcula o novo ponto xk
        i += 1
        
    if armijo == True: print("----Entrou no armijo----")    
    print("Ponto final:\n"                       ,xk               )
    print("Gradiente da função no ponto final:\n",calcGradiente(xk))
    print("Hessiana da função\n"                 ,calcHessiana (xk))
    print("Direção de descida final\n"           ,d                )
    print("Número de iterações:"                 ,i                )
    return

MetodoDeNewton();

