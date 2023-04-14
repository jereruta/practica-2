
nombres = ''''Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR', 'David',
'Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo', 'Francsica',
'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan', 'Joaquina', 'Jorge',
'JOSE', 'Javier', 'Joaquín', 'Julian', 'Julieta', 'Luciana', 'LAUTARO', 'Leonel', 'Luisa',
'Luis', 'Marcos', 'María', 'MATEO', 'Matias', 'Nicolás', 'Nancy', 'Noelia', 'Pablo',
'Priscila', 'Sabrina', 'Tomás', 'Ulises', 'Yanina' '''

notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
          12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
          85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]

notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
          64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
          95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]

# ej A)

def gen_dicc(list1,list2,list3) :
    
    """Esta funcion genera un diccionario cuando se le pasan tres listas
    con la estructura {list1 : [list2 , list2]}"""

    return {key:[val1 , val2] for key, val1, val2 in zip(list1, list2, list3)}
    
                                     
nombres_list = nombres.replace("\n"," ").split("', '")                           # genero lista con los nombres

alumnos_notas = gen_dicc(nombres_list,notas_1,notas_2)                           # genero dicc con nombres y notas

# ej B)

def calc_prom(lista):

    """Esta funcion dada una lista de numeros calcula el promedio simple"""

    return sum(lista)/len(lista)


prom = []                                                                        # genero lista con promedios
for notas in alumnos_notas.values():

    prom.append(calc_prom(notas))

alumnos_promedio = {key : pr for key, pr in zip(nombres_list,prom)}              # genero dicc con nombres y promedios

# ej C)

promedio_gen = calc_prom(prom)                                                   # calculo el promedio del curso
print(f"El promedio general del curso es: {promedio_gen}"[:40])                  

# ej D) 

def max_prom(dicc):

    """Esta funcion toma un diccionario ¿ y devuelve una tupla (key , valor)
    correspondiente al valor maximo del diccionario"""           

    return max(dicc.items(), key = lambda item: (item[1]))     

est_prom_max = max_prom(alumnos_promedio)                        # Busco el promedio mas alto

print(f"Le estudiante con mayor promedio es: {est_prom_max[0]}, con: {est_prom_max[1]}")          

# ej E)

def min_nota(dicc):

    """Esta funcion toma un diccionario y devuelve una tupla (key, valor) 
    correspondiente al valor minimo del diccionario"""

    return min(dicc.items(), key = lambda items: (items[1]))

est_nota_baja = min_nota(alumnos_notas)                          # Busco la nota mas baja

print(f"Le estudiante con nota mas baja es: {est_nota_baja[0]}, con: {min(est_nota_baja[1])}")  




