print("mandejo de funciones v1")
def hola_mundo():
    print("Hola aqui estoy")
def mensa(msg):
    print(msg)
def EscribeNC(nombre,apellido):
    print(nombre,apellido)
    print(f"Tu nombre completo es: {nombre} {apellido}")
def suma2numeros(n1,n2):
    s=n1+n2
    return f"la suma de {n1} + {n2} es de:",s 
# llamado a la funcion
hola_mundo()
mensa("hola whatsapp") # llama a mensa con 1 parametro
mensa("El profe me sorprendio enviando mensajes") # llama a mensa con 1 parametro
EscribeNC("Diego","Ramirez")
print ("Funciones que regresan valores")
print(suma2numeros(7,3))
print(suma2numeros(15,45))