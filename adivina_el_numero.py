#Escribe un programa que almacene un número y pida al usuario adivinarlo.
import random

def jugar():
    repetir = 's'
    while repetir.lower() == 's':
        numero_secreto = random.randint(1, 100)
        num_intentos = 0
        adivinado = False

        print("Bienvenido al juego de Adivina el Número!")
        print("He pensado en un número entre 1 y 100. Intenta adivinar cuál es. ¡Buena suerte!")

        while not adivinado:
            intento = int(input("Introduce tu intento: "))
            num_intentos += 1
            
            if intento < numero_secreto:
                print("El número secreto es mayor!")
            elif intento > numero_secreto:
                print("El número secreto es menor!")
            else:
                adivinado = True
                print(f"¡Felicidades! Has adivinado el número en {num_intentos} intentos.")

        repetir = input("¿Quieres jugar de nuevo? (s/n): ")

    print("Gracias por jugar con nosotros. ¡Adiós!")

if __name__ == "__main__":
    jugar()
