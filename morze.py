# Definir el diccionario para mapear caracteres a código Morse
morse_code_dict = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z',
    '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
    ' ': ' ', '/': '-..-.', '?': '..--..', '!': '-.-.--', '@': '.--.-.', '&': '.-...', '(': '-.--.', ')': '-.--.-', '"': '.-..-.', "'": '.----.', ',': '--..--',
    '$': '...-..-', '¡': '--...-', '¿': '..-.-', '+': '.-.-.', ':': '---...', '.': '.-.-.-', ';': '-.-.-.', '-':'-....-', '=': '-...-', '_': '..--.-'
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

# Función para convertir código Morse a texto
def morse_to_text(morse):
    words = morse.split(' / ')  # Separamos el código Morse en palabras
    text = ''
    for word_morse in words:
        letters_morse = word_morse.split(' ')  # Separamos cada palabra Morse en letras Morse
        word_text = ''
        for letter_morse in letters_morse:
            if letter_morse in morse_code_dict:
                word_text += morse_code_dict[letter_morse]  # Traducir cada letra Morse a texto
            else:
                word_text += '?'  # Si no reconocemos un símbolo Morse, lo representamos con '?'
        text += word_text + ' '  # Agregamos la palabra traducida al texto y un espacio
    return text.strip()  # Eliminamos espacios adicionales al principio y al final

def main():
    texto = input("Ingresa el texto que deseas convertir a código Morse: ").strip()
    if not texto:
        print("El texto ingresado está vacío.")
        return

    resultado = text_to_morse(texto)
    print("El texto traducido a Morse es:", resultado)

def main2():
    morse = input("Ingresa el código Morse que deseas convertir a texto: ").strip()
    if not morse:
        print("El código Morse ingresado está vacío.")
        return

    resultado = morse_to_text(morse)
    print("El código Morse traducido a texto es:", resultado)

if __name__ == "__main__":
    try:
        print("¿Quieres ir de Morse a texto? (si o no) (exit para salir): ")
        p = input("").lower()
        if p == "si" or p == "yes" or p == "y" or p == "s":
            main2()
        elif p == "exit":
            import sys
            sys.exit()
        else:
            main()
    except KeyboardInterrupt:
        sys.exit()
    except Exception as e:
        from tkinter.messagebox import showerror
        showerror(title="Morse", message=f"{e}")
