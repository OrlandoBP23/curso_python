#archivo necesario con todas las funciones para la aplicacion de lineas

def calcular_y(x,m,b):
    '''
    Calcula el valor de y en una linea recta
    x: valor de x
    m: pendiente
    b: interseccion en y
    regresa el valor de y
    '''
    return m*x +b

def test_linea():
    '''
    Prueba de funcionamiento de calcular_y
    '''
    assert calcular_y(0,2,3) == 3

if __name__ == '__main__':
   if test_linea():
    print('Todo bien')
   else:
      print('Todo mal')
      

