# Implementar en el lenguaje de programacion que se desee el algoritmo de descenso por gradiente para minimizar la funcion de Rosenbrock.
#Mostrar una traza de ejecucion hasta convergencia, con rho_k = K/k (dodne K es una constante a determinar empiricamente), 
#inicializando los parametros en el punto (-1, 1)^t.

#Funcion derivada de Wolfram:     export PATH=/opt/anaconda3/bin:$PATH
#derive 10*(y-x^2)^2+(1-x)^2      conda create -n vvv numpy

import sys
import math
import numpy

def DerivadaRosenbrock( x , y ):
    dx = 2*(20*(x**3) - 20*x*y + x - 1)
    dy = 20*(y-(x**2))
    return dx, dy
 
def FuncionRosenbrock(x , y ):
    val = 10*(y-x**2)**2+(1-x)**2
    return val
    
def DistanciaEuclidea(fx , fy , rx , ry ):
    val = math.sqrt((rx - fx)**2 + (ry - fy)**2)
    return val
    
def Gradiente( x , y , k, maxI ):
    fx = x
    fy = y
    solx = x
    soly = y
    for j in range(1, maxI):
        factApr = k/j
        dx,dy = DerivadaRosenbrock(fx,fy)
        rx = fx- dx * factApr
        ry = fy- dy * factApr
        a=numpy.array((fx, fy))
        b=numpy.array((rx, ry))
        try:
            distancia = numpy.linalg.norm(a-b)
            #distancia = DistanciaEuclidea(fx,fy,rx,ry)
            if(distancia <= 0.001):
                solx = fx
                soly = fy
                break
        except:
            print("Peta la distancia")
        finally:
            break
        fx = rx
        fy = ry
        solx = fx
        soly = fy
    return solx, soly

def EncuentraK( x , y , kmin , kmax , step , maxI ):
    listaSol = {}
    i = kmax
    while i >= kmin:
        solx, soly = Gradiente( x , y , i, maxI )
        listaSol[(i)] = {solx,soly}
        i -= step
    for x in listaSol:
    	print(x)

if __name__ == "__main__":
    if len(sys.argv) == 7:
        x = float(sys.argv[1])
        y = float(sys.argv[2])
        kmin = float(sys.argv[3])
        kmax = float(sys.argv[4])
        step = float(sys.argv[5])
        maxI = int(sys.argv[6])
        EncuentraK(x,y,kmin,kmax,step,maxI)
    else:
        syntax()
