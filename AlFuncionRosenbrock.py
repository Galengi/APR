# Implementar en el lenguaje de programación que se desee el algoritmo de descenso por gradiente para minimizar la función de Rosenbrock.
#Mostrar una traza de ejecución hasta convergencia, con rho_k = K/k (dodne K es una constante a determinar empíricamente), 
#inicializando los parámetros en el punto (-1, 1)^t.

#Función derivada de Wolfram:
#derive 10*(y-x^2)^2+(1-x)^2

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
    while i >= kmin:
        for j in range(maxI):
            factApr = i/j
            rx,ry = DerivadaRosenbrock(fx,fy)
            valor = FuncionRosenbrock(fx,fy)
            listaSol[(i,j)]= {fx, fy, rx, ry, valor}
            rx = rx * factApr
            ry = ry * factApr
            if(rx <= 0.001):
                break
            fx = fx - rx
            fy = fy - ry
        i -= step
    return listaSol
            
if __name__ == "__main__":
    if len(sys.argv) == 7:
        x = sys.argv[1]
        y = sys.argv[2]
        kmin = sys.argv[3]
        kmax = sys.argv[4]
        step = sys.argv[5]
        maxI = sys.argv[6]
        DescensoGradiente(x,y,kmin,kmax,step,maxI)
    else:
        syntax()
