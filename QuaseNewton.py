import math
from numpy import *




def f(xk):
    return xk[0][0]**2 + xk[1][0]**2 - 8*xk[0][0] + 5*xk[1][0] + 22.25
def f2(xk):
    return 9*(xk[0][0]**2) - 3*xk[0][0]*xk[1][0] + 1.25*(xk[1][0]**2) - 24*xk[0][0] + 9*xk[1][0] + 22.25
def f3(xk):
    return 0.5*(xk[0][0]**2) + 0.25*(xk[1][0]**2) + 20*math.sin(0.1*xk[0][0]*xk[1][0]) + 0.25
#------------------------------------------------

def calcGradiente(xk):
    return array([    [(2*xk[0][0])-8],
                      [(2*xk[1][0])+5]])
def calcGradiente2(xk):
    return array([    [(18 *xk[0][0]) - (3*xk[1][0]) - 24],
                      [(2.5*xk[1][0]) - (3*xk[0][0]) + 9 ]])
def calcGradiente3(xk):#ESSA FUNÇÃO AQUI DEMORA MUITOOOOOOOOOOOOOOOOO
    return array([    [    xk[0][0] + 2*xk[1][0]*math.cos(0.1*xk[0][0]*xk[1][0])],
                      [0.5*xk[1][0] + 2*xk[0][0]*math.cos(0.1*xk[0][0]*xk[1][0])]])
#------------------------------------------------

def QuaseNewton():

    #------------ VARIÁVEIS -------------------
    t = 1.0; n = 0.25; gama = 0.8; ERRO = 0.0001; i = 0; armijo = False;
    
    xk = array([[2],
                 [2]])
    H  = array([[1,0],
                [0,1]])
    xk_anterior = xk
    gradiente   = calcGradiente(xk)#MUDANÇA AQUI
    g_anterior  = gradiente
    
    #------------ PRINT DE VALORES  -------------------
    print("Ponto inicial:\n"     ,xk               )
    print("F do Ponto inicial:\n",f(xk)            )#MUDANÇA AQUI
    print("Gradiente inicial:\n" ,calcGradiente(xk))#MUDANÇA AQUI


    while(dot(gradiente.transpose(),gradiente)>ERRO ): 
        d  = -dot(H,gradiente)
        while( f(xk+t*d) >  f(xk) + t * n * dot(calcGradiente(xk).transpose(), d) ):#MUDANÇA AQUI
            t = t * gama;
            armijo = True
        xk = xk + t * d
        pk = xk - xk_anterior
        gradiente = calcGradiente(xk)#MUDANÇA AQUI
        qk = gradiente - g_anterior
        H  = H + (dot(pk, pk.transpose()) / dot( pk.transpose(), qk)) - dot(dot(dot(H,qk), qk.transpose()),H) / dot(dot(qk.transpose(), H),qk)
        g_anterior  = gradiente
        xk_anterior = xk
        i += 1

    if armijo == True: print("----Entrou no Armijo----")
    print("Ponto Final:\n"              ,xk               )
    print("F do Ponto Final:\n"         ,f(xk)            )#MUDANÇA AQUI
    print("Gradiente do Ponto Final:\n" ,calcGradiente(xk))#MUDANÇA AQUI
    print("Direção Final:\n"            ,d                )
    print("Número de iterações:"        ,i                )
    
    
QuaseNewton()

