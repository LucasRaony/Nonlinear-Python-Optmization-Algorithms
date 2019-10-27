import math
from numpy import *

def calcGradiente(xk):
    return array([    [2*xk[0][0]],
                      [2*xk[1][0]]])
def calcGradiente2(xk):
    return array([    [(2*xk[0][0])-8],
                      [(2*xk[1][0])+5]])
def calcGradiente3(xk):
    return array([    [(18 *xk[0][0]) - (3*xk[1][0]) - 24],
                      [(2.5*xk[1][0]) - (3*xk[0][0]) + 9 ]])

#-----------------------------------------------------------------------------------------------------------------------------------

def GradientesConjugados(): 
    ERRO = 0.0001; g_anterior = 0; i = 0;
    xk = array([[200],
                [200]])
    A = array([[ 2, 0],
               [ 0, 2]])
    A2 = array([[ 2, 0],
                [ 0, 2]])
    A3 = array([[ 18, -3 ],
                [ -3, 2.5]])
    
    gradiente  = calcGradiente(xk)#MUDA
    d  = -gradiente
    
    print("Xk        inicial:\n",xk       )
    print("Gradiente inicial:\n",gradiente)
    
    while(dot(gradiente.transpose(),gradiente)>ERRO ):
        t  = -dot(gradiente.transpose(),d)/dot( dot(d.transpose(),A), d )#MUDA
        xk = xk + t*d
        g_anterior = gradiente
        gradiente = calcGradiente(xk)#MUDA
        B = dot(dot(d.transpose(),A3),gradiente)/dot( dot(d.transpose(),A3), d )#MUDA
        #B = dot(gradiente.transpose(), gradiente - g_anterior) / dot(g_anterior.transpose(), g_anterior) #POLAK    e RIBIÈRE
        #B = dot(gradiente.transpose(), gradiente)              / dot(g_anterior.transpose(), g_anterior) #FLETCHER e REEVES
        d  = -gradiente + B * d
        i += 1
        
    print("Xk        final:\n"  ,xk       )
    print("Direção   final:\n"  ,d        )
    print("Gradiente final:\n"  ,gradiente)
    print("B         final:\n"  ,B        )
    print("Número de iterações:",i        )
      
    return


GradientesConjugados()

