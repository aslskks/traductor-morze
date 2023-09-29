# Definimos un diccionario que mapea letras y números a su equivalente en código Morse
codigo_morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
}

def texto_a_morse(texto):
    texto = texto.upper()  # Convertimos el texto a mayúsculas para que funcione con letras minúsculas también
    morse = ''
    for caracter in texto:
        if caracter == ' ':
            morse += ' '  # Agregamos un espacio si encontramos un espacio en el texto
        elif caracter in codigo_morse:
            morse += codigo_morse[caracter] + ' '  # Agregamos el código Morse correspondiente y un espacio
        else:
            morse += caracter  # Mantenemos cualquier otro carácter sin cambios
    return morse

def main():
    texto = input("Ingresa el texto que deseas convertir a código Morse: ")
    resultado = texto_a_morse(texto)
    print("El texto en código Morse es:", resultado)

if __name__ == "__main__":
    main()
