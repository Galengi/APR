#Implementar en el lenguaje de programación que se desee el algoritmo de descenso por gradiente para minimizar la función de Rosenbrock.  
#Mostrar una traza de ejecución hasta convergencia, con rho_k = K/k (donde K es una constante a determinar empíricamente), inicializando los parámetros en el punto (-1, 1)^t.

#importamos las librerias sys para que podamos pasarle los parametros a la hora de ejecución
# y la libreria math para hacer la raíz que necesitamos en la función euclídea
import sys
import math

#Función que nos devuevle los valores derivados de las coordenadas x e y de un punto
def DerivadaRosenbrock( x , y ):
    dx = 2*(20*(x**3) - 20*x*y + x - 1)
    dy = 20*(y-(x**2))
    return dx, dy
 
#Función de Rosenbrock que devuelve el valor, pasandole las coordenadas x e y de un punto
def FuncionRosenbrock(x , y ):
    val = 10*(y-x**2)**2+(1-x)**2
    return val
    
#Función que toma como parámetros dos puntos y duevuelve la distáncia euclídea entre esos puntos
def DistanciaEuclidea(fx , fy , rx , ry ):
    val = math.sqrt((rx - fx)**2 + (ry - fy)**2)
    return val

#Función que llamamos para cada k, toma como parámetros un punto(x,y) la k que se está comprobando
#y un máximo de iteraciones
def Gradiente( x , y , k, maxI ):
    #Guardamos los valores iniciales en las variables
    fx = x
    fy = y
    solx = x
    soly = y
    #cont = 0
    for j in range(1, maxI):
        #Por cada iteración reducimos el factor de aprendizaje, que es la magnitud que mueve el punto
        factApr = k/j
        valj = maxI
        try:
            dx,dy = DerivadaRosenbrock(fx,fy)
        except:
            print(dx,dy)
            print("OverflowError: (34, 'Numerical result out of range')")
            break
        #Guardamos los nuevos puntos
        rx = fx- dx * factApr
        ry = fy- dy * factApr
        try:
            distancia = DistanciaEuclidea(fx,fy,rx,ry)
            #Si la distancia es menor que el factor distancia que consideramos solución guardamos 
            #el punto solución y la iteración en la que se ha encontrado solución y terminamos el bucle
            if(distancia <= 0.001):
                solx = fx
                soly = fy
                valj=j
                break
        except:
            print(distancia)
            print("OverflowError: (34, 'Numerical result out of range')")
            break
        
        #Si no ha encontrado solución se sobreescribe el punto anterior por el desplazado y guardamos la solución
        fx = rx
        fy = ry
        #if(cont==1):
        #    solx = fx
        #    soly = fy
        solx = fx
        soly = fy
    return solx, soly, valj

def EncuentraK( x , y , kmin , kmax , step , maxI ):
    #Creamos 3 listas con los valores de k, x e y
    listaK = []
    listaX = []
    listaY = []
    i = kmax
    j = 0
    #Inicializamos las soluciones óptimas por valores que serán sobreescritos.
    jopti = 999
    kopti = 999
    solPunto = (999,999)
    while i >= kmin:
        #Obtenemos el punto solución y su ieración mediante la función anterior, y los añadimos a sus listas
        solx, soly, valj = Gradiente( x , y , i, maxI )
        listaK.append(i)
        listaX.append(solx)
        listaY.append(soly)
        #Si queremos optimizar las iteraciones, nos quedamos con el punto y la k de la menor iteración
        if(valj<jopti):
            jopti=valj
            solPunto=(solx,soly)
            kopti=i
        #Reducimos la k que comprobamos y incrementamos j en 1 por cada solución que añadimos
        i -= step
        j = j +1
    print('Valor de k: ',kopti,'Valor de j: ',jopti,'Punto(',solPunto)
    for x in range(0, j):
        #if(listaX[x] != -1):
        print('Valor de k: ',listaK[x],' Punto(',listaX[x],listaY[x])


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
