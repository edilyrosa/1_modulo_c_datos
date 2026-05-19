
#& 1. IF
#Se ejecuta un bloque si la condición es verdadera.
# Sintaxis: 
# if condición lógica a evaluar :
#   indentación →  código py a ejecutar
#?Sentencia else
# Se usa para definir qué sucede si la condición del if es falsa. 
# Por eso NO LE SIGUE NINGUNA condición lógica a evaluar.  
# Se Ejecuta si ninguna condición previa es verdadera.
#? Ejercicio: Determine si un número es par o impar, 💡solo existen esas 2 posibilidades.
# print('Veamos si un número es par o impar')
# num = int(input('Ingrese el num a evaluar: ')) #*👀
# if num % 2 == 0:
#     print(f'{num} es PAR')
# else:   
#     print(f'{num} es INPAR')
    
    

    
#& 2. ELIF
# Es la forma de intercalar múltiples condiciones a una sentencia if-else. 
#? Ejercicio: catalogue a un estudiante según su calificación, 
# con rangos de {
# +90,  -> # Excelente 🥳
# +80,  -> # Muy bien 👏
# +70,  -> # Bien 👍
# +60,  -> # Suficiente 👌
# else -> # Insuficiente 😞
# }
print('\nDeterminando calificacion de estudiante')


calificacion = int(input('Digite la nota del estudiante: '))

if calificacion < 1 or calificacion >100:
    print('Nota invalida ❌')
elif calificacion >= 90 and calificacion <=100:
    print('Excelente 🥳')
elif calificacion >= 80 and calificacion <90 :
    print('Muy bien 👏')
elif calificacion >= 70 and calificacion <80 :
    print('bien 👏')
elif calificacion >= 60 and calificacion <70 :
    print('Suficiente 👌')
else:
    print('Insuficiente 😞')
    



#& IF - ANIDADOS
# # Determine si usuario puede Conducir?
# # condicion: debe tener licencia (si/no) y ( (ser mayor de edad (>=18)  o estar emancipado (si/no) )

# print('\nDeterminando si usuario puede Conducir?')





# #? TERNARIO
# Es una forma corta de escribir una sentencia if-else en una sola línea.
# Sintaxis: valor_si_verdadero if condición else valor_si_falso
# print('\nAsignamos a una variable bandera de usuario autenticado o no')



# TODO PROXIMO_TEMA:
#  EJERCICIO WEB LOGIN CONDICIONALES Y OPERADORES COMPARACION

    # TIPOS DE DATOS ESTRUCTURALES: LISTAS, TUPLAS, DICCIONARIOS, SETS
    # CILCLOS: FOR, WHILE, BREAK, CONTINUE, RANGE()
