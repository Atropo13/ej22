from collections import namedtuple

# Definición del tipo Persona:
# nombre: Nombre de la persona.
# edad: Edad de la persona en años.
# tiene_licencia: Booleano que indica si la persona tiene licencia de conducir.
# hobbies: Conjunto de hobbies o actividades que le gustan a la persona.
# paises_visitados: Conjunto de países que la persona ha visitado.
# libros_leidos: Lista de libros que la persona ha leído en orden de lectura.
Persona = namedtuple('Persona', ['nombre', 'edad', 'tiene_licencia', 'hobbies', 'paises_visitados', 'libros_leidos'])

juan = Persona('Juan', 20, True, {'fútbol', 'cine'}, {'España', 'Chile'}, ['Don Quijote', 'El Principito'])
maria = Persona('Maria', 15, False, {'lectura', 'música', 'cine'}, {'Francia', 'Chile'}, ['El Principito', '1984'])
pedro = Persona('Pedro', 17, True, {'fútbol', 'natación'}, {'México'}, ['Cien Años de Soledad', 'Moby Dick', '1984'])


print("Juan tiene más de 18 años:",
    juan.edad > 18
)

print("Maria tiene licencia de conducir:",
    maria.tiene_licencia 
)

print("Juan ha visitado Chile:",
    "Chile" in juan.paises_visitados
)

print("A María le gustan el cine y la música:",
    "cine" in maria.hobbies and "música" in maria.hobbies
)

print("'El Principito' es el último libro que ha leído Maria:",
    len(maria.libros_leidos) > 0 and maria.libros_leidos[-1] == "El Principito"
)

print("Ni Juan ni Pedro tienen licencia de conducir:",
    not juan.tiene_licencia and not pedro.tiene_licencia
)

print("Maria ha leído al menos 2 libros:",
    len(maria.libros_leidos) >=2
)

print("María no ha visitado México, pero Pedro sí:",
    "México" not in maria.paises_visitados and "México" in pedro.paises_visitados
)

print("Juan ha leído más libros que María pero menos que Pedro:",
    len(juan.libros_leidos) > len(maria.libros_leidos) and
    len(juan.libros_leidos) < len(pedro.libros_leidos)
)

print("Pedro no ha visitado Chile y tampoco le gusta el cine:",
    "Chile" not in pedro.paises_visitados and "cine" not in pedro.hobbies
)

print("El último libro que María ha leído es '1984' y Juan no lo ha leído aún:",
    len(maria.libros_leidos) > 0 and maria.libros_leidos[-1] == '1984' and '1984' not in juan.libros_leidos
)

print("Pedro ha visitado más países que Juan o ha leído más libros que María:",
    len(pedro.paises_visitados) > len(juan.paises_visitados) or
    len(pedro.libros_leidos) > len(maria.libros_leidos)
)

print("María tiene licencia de conducir o ha leído 'Moby Dick', pero no ambas cosas",
    maria.tiene_licencia or "Moby Dick" in maria.libros_leidos and
    not (maria.tiene_licencia and "Moby Dick" in maria.libros_leidos)
)

print("Juan ha visitado España o Francia, pero no ambos",
    "España" in juan.paises_visitados or "Francia" in juan.paises_visitados and
    not ("España" in juan.paises_visitados and "Francia" in juan.paises_visitados)
)

'''
Para las siguientes expresiones, se precisan dos operadores que aún no hemos estudiado:

Operador de intersección de conjuntos &: devuelve un conjunto con los elementos comunes a los
 dos conjuntos sobre los que se opera.

Método index del tipo list: recibe un valor y devuelve la posición de la lista en la que aparece
 por primera vez dicho valor. ¡CUIDADO! Si no se encuentra el valor en la lista, se produce 
 un error de tipo ValueError.
'''

print("Pedro y Juan comparten al menos un hobby:",
    len(pedro.hobbies & juan.hobbies) > 0
)

print("Juan y María han visitado al menos un país en común o ambos tienen el hobby de ir al cine:",
    len(juan.paises_visitados & maria.paises_visitados)> 0 or
    "cine" in (juan.hobbies & maria.hobbies)
)

print("Juan ha leído 'Don Quijote' antes que 'El Principito':",
    "Don Quijote" in juan.libros_leidos and "El Principito" in juan.libros_leidos and 
    juan.libros_leidos.index("Don Quijote") < juan.libros_leidos.index("El Principito")
)