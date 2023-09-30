# Definimos un diccionario que mapea el código Morse a letras y números
morse_a_texto_dict = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z',
    '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
    ' ': ' ', '/': '-..-.', '?': '..--..', '!': '-.-.--', '@': '.--.-.', '&': '.-...', '(': '-.--.', ')': '-.--.-', '"': '.-..-.', "'": '.----.', ',': '--..--',
    '$': '...-..-', '¡': '--...-', '¿': '..-.-', '+': '.-.-.', ':': '---...', '.': '.-.-.-', ';': '-.-.-.', '-':'-....-', '=': '-...-', '_': '..--.-',
}

def morse_a_texto(morse):
    palabras = morse.split(' / ')  # Separamos el código Morse en palabras
    texto = ''
    for palabra_morse in palabras:
        letras_morse = palabra_morse.split(' ')  # Separamos cada palabra Morse en letras Morse
        palabra_texto = ''
        for letra_morse in letras_morse:
            if letra_morse in morse_a_texto_dict:
                palabra_texto += morse_a_texto_dict[letra_morse]  # Traducimos cada letra Morse a texto
            else:
                palabra_texto += '?'  # Si no reconocemos un símbolo Morse, lo representamos con '?'
        texto += palabra_texto + ' '  # Agregamos la palabra traducida al texto y un espacio
    return texto

def main():
    morse = input("Ingresa el código Morse que deseas convertir a texto: ")
    resultado = morse_a_texto(morse)
    print("El código Morse traducido a texto es:", resultado)

if __name__ == "__main__":
    main()
