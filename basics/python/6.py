text = input("Enter plaintext? ")
shift = int(input("Enter shift? "))

def caesarCipher(text, shift): 
        temp = ""
        for symbol in text:
            if symbol.isalpha():
                alphabet = ord(symbol) + shift

                if alphabet > ord('z'):
                    alphabet -= 26
                final = chr(alphabet) 
                temp += final
        print ("Your ciphertext is: ", (temp))
        return text

caesarCipher(text, shift)