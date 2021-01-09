#Ejercicio uno: escribe un programa simple que simule la operación del
#comando grep en Unix. Debe pedir al usuario que ingrese una expresión
#regular y cuente el número de líneas que coincidan con ésta:
import re
er = input("Ingresa una expresión regular: ")
txt = open("m-box.txt")
x=list()
count = 0
for linea in txt:
    linea = linea.rstrip()
    if re.search('\\b' + er + '\\b', linea):
        count =  count +1
print(count)