# Definir el diccionario para mapear caracteres a código Morse
morse_code_dict = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z',
    '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
    ' ': ' ', '/': '-..-.', '?': '..--..', '!': '-.-.--', '@': '.--.-.', '&': '.-...', '(': '-.--.', ')': '-.--.-', '"': '.-..-.', "'": '.----.', ',': '--..--',
    '$': '...-..-', '¡': '--...-', '¿': '..-.-', '+': '.-.-.', ':': '---...', '.': '.-.-.-', ';': '-.-.-.', '-':'-....-', '=': '-...-', '_': '..--.-',
}

# Función para convertir texto a código Morse
def text_to_morse(text):
    text = text.upper()  # Convertir el texto a mayúsculas
    morse_code = ""
    for char in text:
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + " "  # Agregar un espacio entre cada letra
        else:
            morse_code += " "  # Agregar un espacio para los caracteres desconocidos
    return morse_code

# Ingresar el texto que deseas convertir
texto = input("Ingresa el texto que deseas convertir a código Morse: ")

# Llamar a la función y mostrar el resultado
codigo_morse = text_to_morse(texto)
print("Código Morse resultante: ", codigo_morse)
