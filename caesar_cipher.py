

class CaesarCipher:
    def __init__(self, root, controller):
        return
    
    # Function to encrypte a given string
    def encrypt(self, text):
        shif_value = 22
        encrypted_text = ''

        for i in range(len(text)):
            c = text[i]

            # Encrypt uppercase letters
            if(c.isupper()):
                encrypted_text += chr((ord(c) + shif_value - 65) % 26 + 65)
            # Encrypt lowercase letterss
            elif(c.islower()):
                decrypted_text += chr((ord(c) + shif_value - 97) % 26 + 97)
            # Encrypt numbers
            elif(c.isnumeric()):
                decrypted_text += chr((ord(c) + shif_value - 48) % 26 + 48)
        
        return encrypted_text
    
    def decrypt(self, text):
        shif_value = 22
        decrypted_text = ''

        for i in range(len(text)):
            c = text[i]

            # Decrypt uppercase letters 
            if(c.isupper()):
                decrypted_text += chr((ord(c) - shif_value - 65) % 26 + 65)
            # Decrypt lowercase letters
            elif(c.islower()):
                decrypted_text += chr((ord(c) - shif_value - 97) % 26 + 97)
            # Decrypt Numbers
            elif(c.isnumeric()):
                decrypted_text += chr((ord(c) - shif_value - 48) % 26 + 48)
            
        return decrypted_text

