import sys

def lee_grafo_stdin():
    cant = int(input("Ingrese cantidad de vertices: "))
    
    vertices = []
    aristas = []
    
    for i in range(cant):
        vertices.append(input("Ingrese un vertice: "))
    
    while True:
        text = input("Ingrese una arista: ")
        if text == 'listo':
            break
        text = text.split(' ')
        text = (text[0], text[1])
        aristas.append(text)
    
    return (vertices, aristas)



def cuenta_grado(grafo_lista):
    grados = []

    for vertice in grafo_lista[0]:
        for arista in grafo_lista[1]:
            grados.append(arista.count(vertice))

    for i in range(len(grafo_lista[0])):
        print(f'{(grafo_lista[0])[i]} : {grados[i]}')



def lista_a_adyacencia(grafo_lista):
    print("  ")
    for i in range(len(grafo_lista[0])):
        print(f'{i} ')
    '''
    Transforma un grafo representado por listas a su representacion 
    en matriz de adyacencia.
      A B C
    A 0 0 0
    B 0 0 0
    C 0 0 0
    '''
    
def componentes_conexas(grafo_lista):
    '''
    Dado un grafo en representacion de lista, obtiene sus componentes conexas.
    Ejemplo formato salida: 
        [['a, 'b'], ['c'], ['d']]
    '''
    comp = []
    
    for vertice in grafo_lista[0]:
        for arista in grafo_lista[1]:
            pass
            
    # (['A','B','C'],[('A','B'),('B','C'),('C','B')])

def es_conexo(grafo_lista):
    return len(componentes_conexas(grafo_lista)) == 1

tupla = lee_grafo_stdin()   # Lee el grafo
print (tupla)               # Muestra el grafo
cuenta_grado(tupla)         # Muestra grado de los vertices
lista_a_adyacencia(tupla)   # Muestra matriz de adyacencia
