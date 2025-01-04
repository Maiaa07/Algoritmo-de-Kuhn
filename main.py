# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 17:04:36 2024

@author: maria
"""

def es_matriz_cuadrada(matriz):
    return len(matriz) == len(matriz[0])

def buscar_1_con_asterisco(j,matriz):
    n=len(matriz)
    for columna in range (j,n):
        for fila in range (0,n):
            if matriz [fila][columna]=="1*":
                fila=0
                break
        else:
            return (columna)
    return None

def buscar_1_sin_asterisco(i, j, matriz):
    n = len(matriz)
    for fila in range(i, n):
        if matriz[fila][j] == "1":
            return fila, j
    return None

def buscar_1_con_asterisco_en_filai (i, matriz):
    n=len(matriz)
    for columna in range(0, n):
        if matriz[i][columna] == "1*":
            return i, columna
    return None

def buscar_1_sin_asterisco_en_columnaj (i,j,matriz):
    n=len(matriz)
    for fila in range(i, n):
        if matriz[fila][j] == "1":
            return fila, j
    return None

def crea_cadena_unos(matriz):
    n,p=len(matriz),1
    cadena_unos={f"i_{0}": -(n+2), f"j_{-1}": -(n+2)}
    while p<n:
        cadena_unos[f"i_{p}"]= -(n+2)
        cadena_unos[f"j_{p-1}"]=-(n+2)
        p+=1
    return cadena_unos

def cambiar_1_con_asterisco_por_1_sin_y_viceversa (cadena_unos, k, matriz):
    n=len(matriz)
    matriz[cadena_unos[f"i_{k}"]][cadena_unos[f"j_{k-1}"]]="1*"
    cadena_unos[f"i_{k}"]=-(n+2)
    while k>0:
        matriz[cadena_unos[f"i_{k-1}"]][cadena_unos[f"j_{k-1}"]]="1"
        cadena_unos[f"j_{k-1}"]=-(n+2)
        k-=1
        matriz[cadena_unos[f"i_{k}"]][cadena_unos[f"j_{k-1}"]]="1*"
        cadena_unos[f"i_{k}"]=-(n+2)
    cadena_unos[f"j_{k-1}"]=-(n+2)
    return matriz,k

def deshacer_cadena_epsilon (k,cadena,matriz):
    n,cadena [k]=len(matriz),0
    while k<n-1:
        k+=1
        cadena [k]=0
    return cadena

def fila_esencial (k,cadena_unos,cadena_epsilon,matriz):
    n=len(matriz)
    if cadena_epsilon [cadena_unos[f"i_{k}"]]>0:
        i,j=cadena_unos[f"i_{k}"],cadena_unos[f"j_{k-1}"] 
        cadena_unos[f"i_{k}"],cadena_unos[f"j_{k-1}"]=-(n+2),-(n+2)
        return cadena_epsilon,i,j,cadena_unos
    else: 
        cadena_epsilon[cadena_unos[f"i_{k}"]]=1
        i,j=cadena_unos[f"i_{k}"],cadena_unos[f"j_{k-1}"] 
        cadena_unos[f"i_{k}"],cadena_unos[f"j_{k-1}"]=-(n+2),-(n+2)
        return cadena_epsilon,i,j,cadena_unos
    
def igual_i_a_i_l(i, cadena_unos, l, matriz):
    n = len(matriz)
    for valor in range(l, n):
        if i == cadena_unos[f"i_{l}"]: 
            return i
    return None
#Previo:
def procesar_matriz(matriz):
    maximos_filas = [max(fila) for fila in matriz]
    num_columnas = len(matriz[0])
    maximos_columnas = [max(matriz[fila][col] for fila in range(len(matriz))) for col in range(num_columnas)]
    a = sum(maximos_filas)
    b = sum(maximos_columnas)
    if a <= b:
        lista_u = maximos_filas
        lista_v = [0] * len(maximos_columnas)
    else:
        lista_u = [0] * len(maximos_filas)
        lista_v = maximos_columnas 
    return lista_u, lista_v  
def generar_matriz_unos_y_ceros(matriz, lista_u, lista_v):

    filas = len(matriz)
    columnas = len(matriz[0])
    nueva_matriz = [[0] * columnas for _ in range(filas)] 
    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j] == lista_u[i] + lista_v[j]:
                nueva_matriz[i][j] = 1
    return nueva_matriz

def marcar_uno(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    matriz_char = [[str(val) for val in fila] for fila in matriz]
    columnas_libres = list(range(columnas))
    for i in range(filas):
        for j in columnas_libres[:]:  
            if matriz_char[i][j] == "1":
                matriz_char[i][j] = "1*"
                columnas_libres.remove(j) 
                break  
    return matriz_char
def todo_junto (j,k,l,matriz):
    n=len(matriz)
    cadena_epsilon,cadena_unos=[0] * n,crea_cadena_unos(matriz)
    lista_u,lista_v=procesar_matriz(matriz)
    matriz=marcar_uno(generar_matriz_unos_y_ceros(matriz, lista_u, lista_v))
    while True:
        if buscar_1_con_asterisco(j, matriz) is not None:
            j,i,salir_1=buscar_1_con_asterisco(j,matriz),0,False
            while not salir_1:
                if  buscar_1_sin_asterisco (i,j, matriz):
                    i,j=buscar_1_sin_asterisco (i,j,matriz)
                    cadena_unos [f"i_{k}"],cadena_unos[f"j_{k-1}"],salir_2 = i,j,False
                    while not salir_2:
                        if buscar_1_con_asterisco_en_filai (i,matriz):
                            j,i,salir_3=buscar_1_con_asterisco_en_filai (i,matriz)[1],0,False
                            while not salir_3:
                                if buscar_1_sin_asterisco_en_columnaj (i,j,matriz):
                                    i,j=buscar_1_sin_asterisco_en_columnaj (i,j,matriz)
                                    k+=1
                                    if igual_i_a_i_l (i,cadena_unos,l,matriz):
                                        k-=1
                                        if i<n-1:
                                            i+=1
                                        else:
                                            salir_5=False
                                            while not salir_5:
                                                cadena_epsilon,i,j,cadena_unos=fila_esencial (i,k,n,cadena_unos,cadena_epsilon)
                                                if k>0:
                                                    k-=1
                                                    if i<n-1:
                                                        i+=1
                                                        salir_5=True
                                                else:
                                                    if i<n-1:
                                                        i+=1
                                                        salir_5,salir_3,salir_2=True,True,True
                                                    else:
                                                        salir_5,salir_3,salir_2,salir_1=True,True,True, True
                                                        if j<n-1:
                                                            j+=1
                                                        else:
                                                            return matriz   
                                    else:
                                        l,cadena_unos [f"i_{k}"],cadena_unos[f"j_{k-1}"]=0,i,j
                                        j,salir_3=0,True
                                else:
                                    salir_4=False
                                    while not salir_4:
                                        cadena_epsilon,i,j,cadena_unos=fila_esencial (k,cadena_unos,cadena_epsilon,matriz)
                                        if k>0:
                                            k-=1
                                            if i<n-1:
                                                i+=1
                                                salir_4=True 
                                        else:
                                            if i<n-1:
                                                i+=1
                                                salir_4,salir_3,salir_2=True,True,True
                                            else:
                                                salir_4,salir_3,salir_2,salir_1=True,True,True,True
                                                if j<n-1:
                                                    j+=1
                                                else:
                                                    return matriz                    
                        else:
                            matriz,k=cambiar_1_con_asterisco_por_1_sin_y_viceversa (cadena_unos, k, matriz)
                            cadena_epsilon=deshacer_cadena_epsilon (k,cadena_epsilon,matriz)
                            i,j,k=0,0,0
                            salir_2,salir_1=True,True
                else:
                    if j<n-1:
                        j+=1
                        salir_1=True
                    else:
                        return matriz
        else:
            return matriz

#print(todo_junto(0,0,0,[[10,3,7],[10,1,2],[4,6,6]]))
#print (todo_junto(0,0,0,[[5,3,7],[10,1,2],[4,6,6]]))
#import numpy as np
#matriz = np.random.randint(0, 1000000, (20, 20))
#print(todo_junto(0,0,0,matriz))
#matriz = np.random.randint(0, 1000000, (50, 50))
#print(todo_junto(0,0,0,matriz))










import numpy as np
import time


# Función para medir el tiempo promedio
def medir_tiempos():
    tiempos = []
    
    for _ in range(100):
        # Generamos una nueva matriz
        matriz = np.random.randint(0, 1001, size=(30, 30)).tolist()
        
        # Empezamos el cronómetro
        inicio = time.time()
        
        # Ejecutamos la función global
        todo_junto (0,0,0,matriz)
        
        # Calculamos el tiempo que tardó en ejecutarse
        fin = time.time()
        
        # Guardamos el tiempo
        tiempos.append(fin - inicio)
    
    # Calculamos el tiempo promedio
    tiempo_promedio = np.mean(tiempos)
    
    return tiempo_promedio

# Llamamos a la función para medir el tiempo promedio
tiempo_promedio = medir_tiempos()

# Mostramos el resultado
print(f"El tiempo medio en resolver las asignaciones es: {tiempo_promedio:.6f} segundos.")
