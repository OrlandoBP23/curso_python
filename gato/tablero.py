'''
tablero.py: Dibuja el tablero del juego del gato
'''
import random
 
def dibuja_tablero(simbolos:dict):
    '''  Dibuja el tablero del juego de el gato '''
    print(f'''
    {simbolos['1']} | {simbolos['2']} | {simbolos['3']}
    ---------
    {simbolos['4']} | {simbolos['5']} | {simbolos['6']}
    ---------
    {simbolos['7']} | {simbolos['8']} | {simbolos['9']}
    ''')
 
def ia(simbolos:dict):
    ''' Estrategia de la computadora'''
    ocupado = True
    while ocupado is True:
        if simbolos['5'] not in ['X','O']:
            x = '5'
        else:
            # Elegir aleatoriamente una casilla que esté libre
            disponibles = [key for key, value in simbolos.items() if value not in ['X', 'O']]
            x = random.choice(disponibles)
        
        if simbolos[x] not in ['X', 'O']:  # Verificar si la casilla está vacía
            simbolos[x] = 'O'  # Colocar la 'O' en la casilla seleccionada
            ocupado = False  # Terminar el ciclo
 
def usuario(simbolos:dict):
    ''' Estrategia del usuario '''
    ocupado = True
    lista_numeros = [str(i) for i in range(1,10)] #del 1 al 9
    while ocupado is True:
        x = input('Elija un número del 1 al 9: ')
        if x in lista_numeros:
            if simbolos[x] not in ['X','O']:
                simbolos[x] = 'X'
                ocupado = False
            else:
                print('Esa casilla ya está ocupada')
        else:
            print('Elija un número del 1 al 9')
 
def juego(simbolos:dict, jugador_x: str):
    ''' Juego del gato '''
    lista_combinaciones = [
        ['1','2','3'],
        ['4','5','6'],
        ['7','8','9'],
        ['1','4','7'],
        ['2','5','8'],
        ['3','6','9'],
        ['1','5','9'],
        ['3','5','7']
    ]
    en_juego = True
    dibuja_tablero(simbolos)
    movimientos = 0
    gana = None
    while en_juego:
        usuario(simbolos)
        dibuja_tablero(simbolos)
        movimientos += 1
        gana = checa_winner(simbolos,lista_combinaciones)
        if gana is not None:
            en_juego = False
            continue
        if movimientos >= 9:
            en_juego = False
            continue
        ia(simbolos)
        dibuja_tablero(simbolos)
        movimientos += 1
        gana = checa_winner(simbolos,lista_combinaciones)
        if gana is not None:
            en_juego = False
            continue
        if movimientos >= 9:
            en_juego = False
            continue
    if gana == 'X':
        return jugador_x  
    elif gana == 'O':
        return gana 
    return None
   
 
def checa_winner(simbolos:dict, combinaciones:list):
    ''' Checa si hay un ganador '''
    for c in combinaciones:
        if simbolos[c[0]] == simbolos[c[1]] == simbolos[c[2]]:
            return simbolos[c[0]]
    return None
 
def actualiza_score(score:dict, ganador:str):
    ''' Actualiza el score '''
    X = score["X"]
    O = score["O"]
    
    if ganador is not None:
        print(f'El ganador es {ganador}')
        if ganador == 'X':
            X["G"] += 1  # Sumar un punto a las victorias de X
            O["P"] += 1  # Sumar un punto a las derrotas de O
        elif ganador == 'O':
            O["G"] += 1  # Sumar un punto a las victorias de O
            X["P"] += 1  # Sumar un punto a las derrotas de X
    else:
        # Si es empate
        print('Empate')
        X["E"] += 1  # Sumar un empate a X
        O["E"] += 1  # Sumar un empate a O

 
def despliega_tablero(score:dict):
    ''' Despliega el tablero de score '''
    print(f'''
    X | G: {score["X"]["G"]} | P: {score["X"]["P"]} | E: {score["X"]["E"]}
    O | G: {score["O"]["G"]} | P: {score["O"]["P"]} | E: {score["O"]["E"]}
    ''')
 
if __name__ == '__main__':
    numeros = [str(i) for i in range(1,10)]
    dsimbolos = {x:x for x in numeros}
    g = juego(dsimbolos)
    if g is not None:
        print(f'El ganador es {g}')
    else:
        print('Empate')
   