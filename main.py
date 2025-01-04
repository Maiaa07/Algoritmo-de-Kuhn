# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 17:04:36 2024

@author: maria
"""

from src.funciones import buscar_1_con_asterisco
from src.funciones import buscar_1_sin_asterisco
from src.funciones import buscar_1_con_asterisco_en_filai
from src.funciones import buscar_1_sin_asterisco_en_columnaj
from src.funciones import crea_cadena_unos  
from src.funciones import cambiar_1_con_asterisco_por_1_sin_y_viceversa
from src.funciones import deshacer_cadena_epsilon 
from src.funciones import fila_esencial 
from src.funciones import igual_i_a_i_l
from src.funciones import procesar_matriz
from src.funciones import generar_matriz_unos_y_ceros
from src.funciones import marcar_uno

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
