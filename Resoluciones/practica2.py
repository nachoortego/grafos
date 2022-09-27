import sys

#agrega un vértice a la componente correspondiente
def comp_vert(v, componentes, E):

    componentes.append([v])

    for e in E:
        for componente in componentes:
            if e[0] in componente and e[1] not in componente:
                componente.append(e[1])
            elif e[1] in componente and e[0] not in componente:
                componente.append(e[0])
    return componentes

#verifica si un grafo tiene circuito euleriano (ce)
def verif_tiene_ce(grafo):

    #verifica que el grafo sea conexo

    componentes = []

    for vertice in grafo[0]:
        if not(any(vertice in componente for componente in componentes)):
            componentes = comp_vert(vertice, componentes, grafo[1])

    if(len(componentes)  != 1):
        return False

    #verifica que el grado de todos los vertices sea par

    for vertice in grafo[0]:
      
      suma = 0

      for arista in grafo[1]:
        suma = suma + arista.count(vertice)

      if(suma % 2 != 0):
        return False
        
    #si verifica las cuestiones anteriores tiene un ce, por lo que retorna True
    return True

#verifica si una arista es arista puente
def arista_puente(arista,gradDict):
    try:
        ret = (gradDict[arista[0]] <= 1) or (gradDict[arista[1]] <= 1)
        return ret
    except Exception as e:
        print(f"Error: {e}")

#devuelve un diccionario con el grado de los vértices
def gradosDict(V,E):

    gradDict = {}

    for vertice in V:
        gradDict[vertice] = 0
        for arista in E:
            gradDict[vertice] += 1 if vertice in arista else 0

    return gradDict

def ce(grafo):

    if(verif_tiene_ce(grafo) == False):
        return None

    vertices = grafo[0]
    aristas = grafo[1]

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

            if not arista_puente(arista, gradosDict(vertices,aristas)):

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

if __name__ == '__main__':

    grafoEuleriano = [['a', 'b', 'c'], [('a', 'b'), ('b', 'c'), ('c', 'a')]]
    grafoNoEuleriano = [['a', 'b', 'c','d'], [('a', 'b'), ('c', 'a'), ('b', 'c'),('d', 'a')]]
    grafo_euler = [['a', 'b', 'c', 'd', 'e', 'f'], [('a', 'b'), ('a', 'c'), ('b', 'c'), ('b', 'd'), ('b', 'e'), ('c', 'e'), ('c', 'f'), ('d', 'e'), ('e', 'f')]]