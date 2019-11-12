# Implementar en el lenguaje de programación que se desee el algoritmo de descenso por gradiente para minimizar la función de Rosenbrock.
#Mostrar una traza de ejecución hasta convergencia, con rho_k = K/k (dodne K es una constante a determinar empíricamente), 
#inicializando los parámetros en el punto (-1, 1)^t.

#Función derivada de Wolfram:
#derive 10*(y-x^2)^2+(1-x)^2

import numpy as np


def DerivadaRosenbrock( punto ):
    dx = 2*(20*(punto[0]**3) - 20*punto[0]*punto[1] + punto[0] - 1)
    dy = 20*(punto[1]-(punto[0]**2))
    return dx, dy
 

def DescensoGradiente( x , y , maxI ):
    punto = np.array([x, y])
    
    for i in range(100):
        for j in range(maxI):
            factApr = i/j
            funDer = np.array(DerivadaRosenbrock(punto))
            punto = punto - np.dot(factApr,funDer)
            
            
            
if __name__ == "__main__":
    if len(sys.argv) == 4:
        x = sys.argv[1]
        y = sys.argv[2]
        maxI = sys.argv[3]
        DescensoGradiente(x,y,maxI)
    else:
        syntax()
