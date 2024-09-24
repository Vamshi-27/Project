# Morse-Code Encryption and Decryption

Morse_code_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....','I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-',' ':'-.-.-'}

Morse_code_dict1 = {value: key for key, value in Morse_code_dict.items()}
def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != '':
            cipher += Morse_code_dict[letter] + ','
        else:
            cipher += ','
    return cipher

def decrypt(message):
    decipher = ''
    code= message.split(',')
    for letter in code:
        if letter != '':
            decipher += Morse_code_dict1[letter]
    return decipher

def main():
    n=input("Press e to encrypt and d to decrypt:").lower()
    if n=='e':
        message = input("Enter the message to encrypt: ").upper()
        result = encrypt(message)
        print (result)
    elif n=='d':
        message = input("Enter the message to decrypt: ")
        result = decrypt(message)
        print (result)
    else:
        print("Invalid Input")

if __name__ == '__main__':
    main()