#! /usr/bin/python
# -*- coding: utf-8 -*-

# 2da Practica Laboratorio 
# Teoria de Grafos
# Consigna: Implementar los siguientes metodos

import sys

def lee_grafo_stdin():
    '''
    Lee un grafo desde entrada estandar y devuelve su representacion como lista.
    Ejemplo Entrada: 
        3
        A
        B
        C
        A B
        B C
        C B
    Ejemplo retorno: 
        (['A','B','C'],[('A','B'),('B','C'),('C','B')])
    '''

    vertices = []
    aristas = []

    print("Ingrese los vertices y cuando termine aprete espacio:")

    for line in sys.stdin:
        if line == '\n':
            break
        else:
            # Con strip() eliminamos los '\n' del final de c/line
            vertices.append(line.strip())

    print("Ingrese las aristas y cuando termine aprete espacio:")

    for line in sys.stdin:
        if line == '\n':
            break
        else:
            # Con strip() eliminamos los '\n' del final de c/line
            aristas.append(line.strip())

    grafo = [[],[]]

    grafo[0] = vertices
    grafo[1] = aristas

    return grafo

    pass

def modif_list(v, componentes, E):

    componentes.append([v])

    for e in E:
        for componente in componentes:
            if e[0] in componente and e[1] not in componente:
                componente.append(e[1])
            elif e[1] in componente and e[0] not in componente:
                componente.append(e[0])
    return componentes



"""Comprueba si un grafo no dirigido tiene un circuito euleriano."""
def graph_has_eulerian_circuit(graph):

    # Verifico que sea conexo

    componentes = []

    for vertice in graph[0]:
        if not(any(vertice in componente for componente in componentes)):
            componentes = modif_list(vertice, componentes, graph[1])

    if(len(componentes)  != 1):
        return False

    # Verifico que el grado de todos los vertices sea par
    suma = 0

    for vertice in graph[0]:
      suma = 0
      for arista in graph[1]:
        suma = suma + arista.count(vertice)

      if(suma % 2 != 0):
        return False
        
    # Finalmente returna True si existe un circuito euleriano
    return True


def arista_puente(frontera,listGrados):
    try:
        ret = (listGrados[frontera[0]] <= 1) or (listGrados[frontera[1]] <= 1)
        return ret
    except Exception as e:
        print(f"Error: {e}")

def listaGrados(V,E):

    diccionarioGrados = {}

    for vertice in V:
        diccionarioGrados[vertice] = 0
        for frontera in E:
            diccionarioGrados[vertice] += 1 if vertice in frontera else 0

    return diccionarioGrados

def find_eulerian_circuit(graph):

    if(graph_has_eulerian_circuit(graph) == False):
        return None

    vertices = graph[0]
    aristas = graph[1]

    verticeInicio = vertices[0]
    circuitoEuler = []

    for arista in aristas:
        if arista[0] == verticeInicio or arista[1] == verticeInicio:
            
            if arista[0] == verticeInicio:
                verticeEntra = arista[0]
                verticeSale = arista[1]
            else:
                verticeEntra = arista[1]
                verticeSale = arista[0]

            if not arista_puente(arista,listaGrados(vertices,aristas)):
                circuitoEuler.append((verticeEntra,verticeSale))
                aristas.remove(arista)
                verticeEntra = verticeSale
    
    while aristas != []:
        for arista in aristas:
            if arista[0] == verticeInicio or arista[1] == verticeInicio:
                if arista[0] == verticeInicio:
                    verticeEntra = arista[0]
                    verticeSale = arista[1]
                else:
                    verticeEntra = arista[1]
                    verticeSale = arista[0]

                circuitoEuler.append((verticeEntra,verticeSale))
                aristas.remove(arista)
                verticeInicio =verticeSale


    return circuitoEuler
     
    pass


def main():

    grafoEuleriano = [['a', 'b', 'c'], [('a', 'b'), ('b', 'c'), ('c', 'a')]]
    grafoNoEuleriano = [['a', 'b', 'c','d'], [('a', 'b'), ('c', 'a'), ('b', 'c'),('d', 'a')]]
    grafo_euler = [['a', 'b', 'c', 'd', 'e', 'f'], [('a', 'b'), ('a', 'c'), ('b', 'c'), ('b', 'd'), ('b', 'e'), ('c', 'e'), ('c', 'f'), ('d', 'e'), ('e', 'f')]]
    print(find_eulerian_circuit(grafoEuleriano))

    pass

if __name__ == '__main__':
    main()