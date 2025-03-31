#exercise1#
perro = {}
#exercise2#
perro = {'nombre':'guero',
       'color':'claro',
       'raza':'Chihuahua',
       'piernas':4,
       'edad':1}
#exercise3#
estudiambre = {
    'Nombre':'Jesus',
    'Apellido':'Villalobos',
    'Genero':'Hombre',
    'edad':19,
    'estado matrimonial':'soltero',
    'Habilidades':['Python','Nadar','HTML','CSS','JS'],
    'Pais':'Mexico',
    'Ciudad':'Zacatecas',
    'Dirreccion':{
        'Calle':'Juan de montoro ',
        'Casa':'304',
    }
}
#exercise4#
print(f'The lenght of the student dictionary is {len(estudiambre)}')
print(f'The data type of student skills is {type(estudiambre["Habilidades"])}')
#exercise5#
estudiambre['Habilidades'].append('PHP')
print(estudiambre['Habilidades'])
#exercise6#
keyList = list(estudiambre.keys())
print(keyList)
#exercise7#
valList = list(estudiambre.values())
print(valList)
#exercise8,9#
estudTuple = estudiambre.items()
print(estudTuple)
#exercise10#
estudiambre.pop('Genero')
print(estudiambre)
#exercise11#
del perro