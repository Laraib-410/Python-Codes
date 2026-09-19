#Build a Ceasar Cipher:
def caesar(text, shift, encrypt=True):     #user-defined function
    if not isinstance(shift, int): 
        return 'Shift must be an integer value.'
    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if not encrypt:
        shift = - shift
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    encrypted_text = text.translate(translation_table)
    return encrypted_text
#function for encryption:
def encrypt(text, shift):
    return caesar(text, shift)
#function for decryption:
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)
encrypted_text ='Pbhentr vf sbhaq va hayvxryl cynprf.'
print(encrypted_text)
decrypted_text=decrypt(encrypted_text,13)
print(decrypted_text)