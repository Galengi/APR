# Implementar en el lenguaje de programación que
se desee el algoritmo de descenso por gradiente para minimizar la
función de Rosenbrock.  Mostrar una traza de ejecución hasta
convergencia, con rho_k = K/k (dodne K es una constante a determinar
empíricamente), inicializando los parámetros en el punto (-1, 1)^t.

import numpy as np


def DerrivRosenbrock1 ( point ):
    dx = (-2*(1 - point[0]) - 400*(point[1] - (point[0]**2)**2))
    dy = 200*(point[1] - (point[0]**2))
    return dx, dy
 


if __name__ == "__main__":
    if len(sys.argv) == 3:
        colNot = ""
        colNot += sys.argv[1]
        savIndx = sys.argv[2]
        indexer(colNot, savIndx)
    else:
        syntax()
