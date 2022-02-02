#Generador de contraseñas aleatorias.
import random 
import string

#Se introduce la longuitud que quieres para la contraseña.
length = int(input("Ingresa longitudde la contraseña: "))

#Te genera la contraseña aleatoriamente con la longuitud elegida.
caracteres = string.ascii_lowercase + string.digits + string.ascii_letters + string.ascii_uppercase + string.punctuation
result_str = ''.join(random.choice(caracteres) for i in range(length))
print("La contraseña de longitud", length, "es:", result_str)

#input para el sitio en el que se usa la contraseña.
passSite = str(input("Para donde es la contraseña: "))

#Te crea un archivo donde te muestra las contraseñas generadas.
try:
    with open('desktop/Password.txt', 'w') as f:
        f.write('Estas es tu contraseña:\n')
        f.write('La contraseña ')
        f.write(passSite)
        f.write(' es: ')
        f.write(result_str)
        print('Se ha creado el archivo donde se guarda tu contraseña!')
except FileNotFoundError:
    print("El documento no existe o no se ha podido crear")