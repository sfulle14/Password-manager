

class CaesarCipher:
    def __init__(self, root, controller):
        return
    
    # Function to encrypte a given string
    def encrypt(self, text):
        shif_value = 22
        encrypted_text = ''

        for c in enumerate(text):
            # Encrypt uppercase letters
            if(c.isupper()):
                encrypted_text += chr((ord(c) + shif_value - 65) % 26 + 65)

            # Encrypt lowercase letterss
            else:
                encrypted_text += chr((ord(c) + shif_value - 97) % 26 + 97)
        
        return encrypted_text
    
    def decrypt(self, text):
        shif_value = 22
        decrypted_text = ''

        for c in enumerate(text):
            # Decrypt uppercase letters 
            if(c.isupper()):
                decrypted_text += chr((ord(c) - shif_value + 65) % 26 - 65)
            # Decrypt lowercase letters
            else:
                decrypted_text += chr((ord(c) - shif_value + 97) % 26 - 97)

        return decrypted_text

