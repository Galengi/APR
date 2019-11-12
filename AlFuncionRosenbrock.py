# Implementar en el lenguaje de programación que se desee el algoritmo de descenso por gradiente para minimizar la función de Rosenbrock.
#Mostrar una traza de ejecución hasta convergencia, con rho_k = K/k (dodne K es una constante a determinar empíricamente), 
#inicializando los parámetros en el punto (-1, 1)^t.

#Función derivada de Wolfram:
#derive 10*(y-x^2)^2+(1-x)^2

def DerivadaRosenbrock( x , y ):
    dx = 2*(20*(x**3) - 20*x*y + x - 1)
    dy = 20*(y-(x**2))
    return dx, dy
 

def DescensoGradiente( x , y , maxI ):
    fx = x
    fy = y
    listaSol = {}
    for i in range(100):
        listaSol[i] = {}
        for j in range(maxI):
            factApr = i/j
            rx,ry = DerivadaRosenbrock(fx,fy)
            rx = rx * factApr
            ry = ry * factApr
            fx = fx - rx
            fy = fy - ry
            listaSol[i][j] = {fx, fy}
    return listaSol
            
if __name__ == "__main__":
    if len(sys.argv) == 4:
        x = sys.argv[1]
        y = sys.argv[2]
        maxI = sys.argv[3]
        DescensoGradiente(x,y,maxI)
    else:
        syntax()
