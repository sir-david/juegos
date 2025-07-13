import os
import random


def cargar_palabras(ruta="words.txt"):
    with open(os.path.join(os.path.dirname(__file__), ruta), "r", encoding="utf-8") as f:
        return [palabra.strip() for palabra in f if palabra.strip()]


def elegir_palabra(palabras):
    return random.choice(palabras)


def mostrar_estado(palabra, letras_adivinadas):
    return " ".join([letra if letra in letras_adivinadas else "_" for letra in palabra])


def juego():
    palabras = cargar_palabras()
    palabra = elegir_palabra(palabras)
    vidas = int(os.getenv("AHORCADO_VIDAS", 5))
    letras_adivinadas = set()
    letras_intentadas = set()

    while vidas > 0 and set(palabra) != letras_adivinadas:
        print("\nPalabra:", mostrar_estado(palabra, letras_adivinadas))
        print("Vidas restantes:", vidas)
        print("Letras intentadas:", ", ".join(sorted(letras_intentadas)))
        intento = input("Ingresa una letra: ").strip().lower()

        if len(intento) != 1 or not intento.isalpha():
            print("Entrada inválida. Ingresa solo una letra.")
            continue
        if intento in letras_intentadas:
            print("Ya intentaste esa letra. Elige otra.")
            continue

        letras_intentadas.add(intento)

        if intento in palabra:
            letras_adivinadas.update({letra for letra in palabra if letra == intento})
            print("¡Correcto!")
        else:
            vidas -= 1
            print("Incorrecto. Pierdes una vida.")

    if set(palabra) == letras_adivinadas:
        print("\n¡Ganaste! La palabra era:", palabra)
    else:
        print("\n¡Perdiste! La palabra era:", palabra)


if __name__ == "__main__":
    while True:
        juego()
        jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): ").strip().lower()
        if jugar_de_nuevo != "s":
            break
