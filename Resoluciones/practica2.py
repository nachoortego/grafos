import sys

def comp_vert(v, componentes, E):

    componentes.append([v])

    for e in E:
        for componente in componentes:
            if e[0] in componente and e[1] not in componente:
                componente.append(e[1])
            elif e[1] in componente and e[0] not in componente:
                componente.append(e[0])
    return componentes

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

if __name__ == '__main__':

    grafoEuleriano = [['a', 'b', 'c'], [('a', 'b'), ('b', 'c'), ('c', 'a')]]
    grafoNoEuleriano = [['a', 'b', 'c','d'], [('a', 'b'), ('c', 'a'), ('b', 'c'),('d', 'a')]]
    grafo_euler = [['a', 'b', 'c', 'd', 'e', 'f'], [('a', 'b'), ('a', 'c'), ('b', 'c'), ('b', 'd'), ('b', 'e'), ('c', 'e'), ('c', 'f'), ('d', 'e'), ('e', 'f')]