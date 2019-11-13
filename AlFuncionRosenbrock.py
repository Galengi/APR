# Implementar en el lenguaje de programacion que se desee el algoritmo de descenso por gradiente para minimizar la funcion de Rosenbrock.
#Mostrar una traza de ejecucion hasta convergencia, con rho_k = K/k (dodne K es una constante a determinar empiricamente), 
#inicializando los parametros en el punto (-1, 1)^t.

#Funcion derivada de Wolfram:
#derive 10*(y-x^2)^2+(1-x)^2

import sys

def DerivadaRosenbrock( x , y ):
    dx = 2*(20*(x**3) - 20*x*y + x - 1)
    dy = 20*(y-(x**2))
    return dx, dy
 
def FuncionRosenbrock(x , y ):
    val = 10*(y-x**2)**2+(1-x)**2
    return val
    
def DescensoGradiente( x , y , kmin, kmax, step, maxI ):
    fx = x
    fy = y
    listaSol = {}
    i = kmax
    kvol=9999
    soli=9999
    while i >= kmin:
    	sol = 999
        for j in range(1, maxI):
            factApr = i/j
            rx,ry = DerivadaRosenbrock(fx,fy)
            valor = FuncionRosenbrock(fx,fy)
            listaSol[(i,j)]= {fx, fy, rx, ry, valor}
            rx = rx * factApr
            ry = ry * factApr
            if(rx <= 0.001):
                if(sol > j):
            	    sol = j
                break
            fx = fx - rx
            fy = fy - ry
        if(soli > sol):
            soli = sol
            kvol = i
        i -= step
    print (soli)
    print (kvol)
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
        DescensoGradiente(x,y,kmin,kmax,step,maxI)
    else:
        syntax()
