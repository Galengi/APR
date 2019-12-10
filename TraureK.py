#Implementar en el lenguaje de programacion que se desee el algoritmo de descenso por gradiente para minimizar la funcion de Rosenbrock.  
#Mostrar una traza de ejecucion hasta convergencia, con rho_k = K/k (donde K es una constante a determinar empiricamente), inicializando los parametros en el punto (-1, 1)^t.

#importamos las librerias sys para que podamos pasarle los parametros a la hora de ejecucion
# y la libreria math para hacer la raiz que necesitamos en la funcion euclidea
import sys
import math

#Funcion que nos devuelve los valores derivados de las coordenadas x e y de un punto
def DerivadaRosenbrock( x , y ):
    dx = 2*(20*(x**3) - 20*x*y + x - 1)
    dy = 20*(y-(x**2))
    return dx, dy
 
#Funcion de Rosenbrock que devuelve el valor, pasandole las coordenadas x e y de un punto
def FuncionRosenbrock(x , y ):
    val = 10*(y-x**2)**2+(1-x)**2
    return val
    
#Funcion que toma como parametros dos puntos y duevuelve la distancia euclidea entre esos puntos
def DistanciaEuclidea(fx , fy , rx , ry ):
    val = math.sqrt((rx - fx)**2 + (ry - fy)**2)
    return val

#Funcion que llamamos para cada k, toma como parametros un punto(x,y) la k que se esta comprobando
#y un maximo de iteraciones
def Gradiente( x , y , k, maxI ):
    #Guardamos los valores iniciales en las variables
    fx = x
    fy = y
    solx = x
    soly = y
    cont = 0
    for j in range(1, maxI):
        #Por cada iteracion reducimos el factor de aprendizaje, que es la magnitud que mueve el punto
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
            #Si la distancia es menor que el factor distancia que consideramos solucion guardamos 
            #el punto solucion y la iteracion en la que se ha encontrado solucion y terminamos el bucle
            if(distancia <= 0.00001):
                solx = fx
                soly = fy
                valj=j
                cont = 1
                break
        except:
            print(distancia)
            print("OverflowError: (34, 'Numerical result out of range')")
            break
        
        #Si no ha encontrado solucion se sobreescribe el punto anterior por el desplazado y guardamos la solucion
        fx = rx
        fy = ry
        if(cont==1):
            solx = fx
            soly = fy
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
    #Inicializamos las soluciones optimas por valores que seran sobreescritos.
    jopti = 999
    kopti = 999
    solPunto = (999,999)
    while i >= kmin:
        #Obtenemos el punto solucion y su iteracion mediante la funcion anterior, y los anadimos a sus listas
        solx, soly, valj = Gradiente( x , y , i, maxI )
        listaK.append(i)
        listaX.append(solx)
        listaY.append(soly)
        #Si queremos optimizar las iteraciones, nos quedamos con el punto y la k con la menor iteracion
        if(valj<jopti):
            jopti=valj
            solPunto=(solx,soly)
            kopti=i
        #Reducimos la k que comprobamos y incrementamos j en 1 por cada solucion que anadimos
        i -= step
        j = j +1
    print('Valor de k: ',kopti,'Valor de j: ',jopti,'Punto(',solPunto)
    for x in range(0, j):
        if(listaX[x] != -1):
        #pintarTraza(x , y , kopti , maxI)
            pintarTraza(x , y , listaK[x] , maxI)
        #print('Valor de k: ',listaK[x],' Punto(',listaX[x],listaY[x])

def pintarTraza( x , y , k, maxI ):
    #Guardamos los valores iniciales en las variables
    fx = x
    fy = y
    solx = x
    soly = y
    listaX = []
    listaY = []
    j = 0
    listaX.append(fx)
    listaY.append(fy)
    for j in range(1, maxI):
        #Por cada iteracion reducimos el factor de aprendizaje, que es la magnitud que mueve el punto
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
            #Si la distancia es menor que el factor distancia que consideramos solucion guardamos 
            #el punto solucion y la iteracion en la que se ha encontrado solucion y terminamos el bucle
            if(distancia <= 0.00001):
                solx = fx
                soly = fy
                j = j +1
                break
        except:
            print(distancia)
            print("OverflowError: (34, 'Numerical result out of range')")
            break
        
        #Si no ha encontrado solucion se sobreescribe el punto anterior por el desplazado y guardamos la solucion
        fx = rx
        fy = ry
        solx = fx
        soly = fy
        j = j +1
        listaX.append(solx)
        listaY.append(soly)
    for x in range(0, j):
        print('Iteracion: ',x,' Punto(',listaX[x],listaY[x])
    
    

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
