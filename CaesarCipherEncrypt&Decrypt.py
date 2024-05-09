print("Welcome to Encryption and Decryption Program")
text = input("Enter the text you want to encrypt or decrypt: ")
print("""Choose Operation
1.Encrypt
2.Decrypt""")
operation = int(input("Enter your choice(1 or 2): "))
shift = int(input("Enter the shift number: "))
def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            # Shift only letters
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)
if(operation == 1):
    print("Result :" + encrypt(text,shift))
if(operation == 2):
    print("Result :" + decrypt(text,shift))