# Exercises: Level 1#
#exercise1#
EDAD = int(input(f'Ingrese su edad: '))
if EDAD >= 18:
    print(f'Puedes manejar')
else:
    print(f'necesitas mas edad')
#exercise2#
YO = int(input("Enter your age: "))
TU = 20

if YO > TU:
    print(f"Soy mas grande que tu")
elif TU < YO:
    print(f"Eres mas grande que yo")
else:
    print(f'Tenemos la misma edad ')

#exercise3#
n1 = int(input(f"INGRESE UN NUMERO: "))
n2 = int(input(f"INGRESE UN NUMERO: "))

if n1 > n2:
    print(f"{n1} ES MAYOR QUE {n2}")
elif n1 < n2:
    print(f"{n2} ES MAYOR QUE {n1}")
else:
    print(f'Son el mismo')
# Exercises: Level 2#
#exercise1#
puntaje = int(input("Ingrese su puntaje: "))

if puntaje < 50:
    print(f"Grado F")
elif puntaje <= 59 and puntaje >= 50:
    print(f"Grado D")
elif puntaje <= 69 and puntaje >= 60:
    print(f"Grado C")
elif puntaje <= 89 and puntaje >= 70:
    print(f"Grado B")
elif puntaje <= 100 and puntaje >= 90:
    print(f"Grado A")
else:
    print(f"Sintax error")
#exercise2#
mes = input("Enter the current month: ").upper()

if mes == "Septiembre" or mes == "Octubre" or mes == "Noviembre":
    print(f"La temporada actual es otoño")

elif mes == "Diciembre" or mes == "Enero" or mes == "Febrero":
    print(f"La temporada actual es invierno")

elif mes == "Marzo" or mes == "Abril" or mes == "Mayo":
    print(f"La temporada actual es primavera")

elif mes == "Junio" or mes == "Julio" or mes == "Agosto":
    print(f"La temporada actual es verano")

else:
    print(f"Sintax error")

#exercise3#
frutas = ['platano', 'naranja', 'mango', 'limon']
newfrutas = input("Ingrese frutas: ").lower()

if newfrutas in frutas:
    print(f"Las {newfrutas} estan en la lista: ")
else:
    print(f"Agregando {newfrutas}...")
    frutas.append(newfrutas)
print(frutas)
# Exercises: Level 3#
#exercise1#
persona = {
    'Nombre': 'Jesús',
    'Apellido': 'Alejandro',
    'Edad': 19,
    'Pais': 'Mexico',
    'EstadoMatrimonial': False,
    'Habilidades': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'DIRECCIÓN': {
        'Calle': 'Mondongo',
        'código postal': '34510'
    }
}
if 'Habilidades' in persona.keys():
    mid = int(len(persona['Habilidades'])/2)
    print(persona['skills'][mid])
else:
    print(f"'Habilidades' no está en la persona")

if 'Habilidades' in persona.keys():
    if "Python" in persona['Habilidades']:
        print(f"Python es una habilidad en el diccionario")
    else:
        print(f"Python no es una habilidad en el diccionario")
else:
    print(f"'skills' no está en la persona")


fronDev = ['JavaScript','React']
backDev = ['Node','Python','MongoDB']
fullStack = ['React', 'Node', 'MongoDB']

if persona['skills'] == fronDev:
    print(f"El es un desarrollador front-end")
elif persona['skills'] == backDev:
    print(f"El es un desarrollador back-end")
elif persona['skills'] == fullStack:
    print(f"El es un desarrollador fullstack")
else:
    print(f"Titulo desconocido")



if persona['EstadoMatrimonial']:
    status = "Esta Casado"
else:
    status = "El NO esta casado"

print(f"{persona['Nombre']} {persona['Apellido']} vive en {persona['Pais']}. {status} ")
