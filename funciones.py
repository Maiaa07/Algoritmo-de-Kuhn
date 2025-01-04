# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 17:06:54 2024

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