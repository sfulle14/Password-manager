

class CaesarCipher:
    def __init__(self, root, controller):
        return
    
    # Function to encrypte a given string
    def encrypt(self, text):
        shift_value = 22
        shift_num = 3
        encrypted_text = ''

        for i in range(len(text)):
            c = text[i]

            # Encrypt uppercase letters
            if(c.isupper()):
                encrypted_text += chr((ord(c) + shift_value - 65) % 26 + 65)
            # Encrypt lowercase letterss
            elif(c.islower()):
                encrypted_text += chr((ord(c) + shift_value - 97) % 26 + 97)
            # Encrypt numbers
            elif(c.isnumeric()):
                encrypted_text += chr((ord(c) + shift_num - 48) % 10 + 48)
            # Handle all other values
            else:
                encrypted_text += c

        
        return encrypted_text
    
    def decrypt(self, text):
        shift_value = 22
        shift_num = 3
        decrypted_text = ''

        for i in range(len(text)):
            c = text[i]

            # Decrypt uppercase letters 
            if(c.isupper()):
                decrypted_text += chr((ord(c) - shift_value - 65) % 26 + 65)
            # Decrypt lowercase letters
            elif(c.islower()):
                decrypted_text += chr((ord(c) - shift_value - 97) % 26 + 97)
            # Decrypt Numbers
            elif(c.isnumeric()):
                decrypted_text += chr((ord(c) - shift_num - 48) % 10 + 48)
            # Handle all other values
            else:
                decrypted_text += c

        return decrypted_text

