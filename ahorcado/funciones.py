'''
funciones auxiliares del juego Ahorcado
'''

def carga_archivo_texto(archivo:str)-> list:
    '''
    Carga un archivo de texto y devuelveuna lista con las oraciones del archivo
    '''

    with open(archivo, 'r', encoding='utf-8') as file:
        oraciones = file.readlines()
    return oraciones  

def carga_plantillas(nombre_plantilla)->dict:
    '''
    Carga las plantillas del juego a partir de un archivo de un texto
    '''  
    plantillas = {}
    for i in range(6):
        plantillas[i] = carga_archivo_texto(f'./plantillas/{nombre_plantilla}-{i}.txt')
    return plantillas

def despliega_plantilla(diccionario:dict, nivel:int):
    '''
    Despliega una planitilla del juego
    '''
    if nivel <=5:
        template = diccionario[nivel]
        for renglon in template:
            print(renglon)

if __name__ == '__main__':
    plantilla = carga_plantillas('plantilla')
    despliega_plantilla(plantilla,5)
    lista_oraciones = carga_archivo_texto('./datos/pg15532.txt')
    print(lista_oraciones[50:60])
    texto = "".join(lista_oraciones[110:])
    print(texto[:100])
    

