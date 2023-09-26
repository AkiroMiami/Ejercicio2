print("hola mundo") #hola mundo perron
print("rama practica") #soy el miami
#Nombre Andre Ahumada Avila (Miami)

#Esta sirve para el desarrollo
def cambiar_letras(palabra):
    nueva_palabra = ""
    for letra in palabra:
        if letra == 'm':
            nueva_palabra += 'M'
        elif letra == 'i':
            nueva_palabra += 'I'
        elif letra == 'a':
            nueva_palabra += 'A'
        else:
            nueva_palabra += letra
    return nueva_palabra

# Ejemplo de uso:
palabra_original = "miami"
nueva_palabra = cambiar_letras(palabra_original)
print(nueva_palabra)  # Esto imprimirá "MaIAMI"
