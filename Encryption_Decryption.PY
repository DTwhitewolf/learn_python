Text = 'hallo world'
custom_key = 'python'

def vigenere(message, key, direction=1) :
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():
        #append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:
            #find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1
            #define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset * direction) % len(alphabet)
            final_message += alphabet[new_index]
    return final_message

def encrypt(message, key):
    return vigenere(message, key)

def decrypt(message, key):
    return vigenere(message, key, -1)

decryption = decrypt(Text, custom_key)

print(f"\nEncryption text: {Text}")
print(f"\ndecrypted text: {decryption}")