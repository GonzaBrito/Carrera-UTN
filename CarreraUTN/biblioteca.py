from copy import deepcopy

def ordenamiento(lista_personajes:list, ordenar_por:str, sentido:bool)-> list:
    copia_lista_personajes = deepcopy(lista_personajes)
    copia_lista_personajes.sort(key = lambda personaje: personaje[ordenar_por], reverse = sentido)
    return copia_lista_personajes