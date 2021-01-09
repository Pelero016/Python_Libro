def switch(order, arreglo):
    lista = order.split()
    orden = lista[0]
    if orden == "print":
        print(arreglo)
        return arreglo
    elif orden == "insert":
        value = int(lista[2])
        posicion = int(lista[1])
        arreglo.insert(posicion, value)
        return arreglo
    elif orden == "append":
        arreglo.append(int(lista[1]))
        return arreglo
    elif orden == "remove":
        arreglo.remove(int(lista[1]))
        return arreglo
    elif orden == "pop":
        arreglo.pop()
        return arreglo
    elif orden == "sort":
        arreglo.sort()
        return arreglo
    elif orden == "reverse":
        arreglo.reverse()
        return arreglo
    else:
        pass


value = int(input())
lista = list()
for _ in range(value):
    order = input()
    lista = switch(order, lista)
#################Another Form a lot much easier########################3
n = input()
l = []
for _ in range(n):
    s = input().split()  # guardo una lista con la entrada particionada
    cmd = s[0]  # El comando será el primer valor de la lista
    args = s[1:]  # Los argumentos serán los valores siguientes
    if cmd != "print":  # si el comando es diferente de print
        cmd += "(" + ",".join(args) + ")"  # concateno el comando con los argumentos creando la cadena paso a paso
        # ",".joins(args) concatena los argumentos separandolos por comas sin espacio
        eval(
            "l." + cmd)  # Ejecuta la expresión del argumento en este caso l.append(value) o l.insert(value,posicion) etc.
    else:
        print
        l
