class caesar:
    def __init__(self):
        pass
    def encode(self, plain_text,password):  #Function to Encode Like a Caesar Cipher
        alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        code_text = ""
        for letter in plain_text:                         #Loop to encode message
            if letter == " ":
                code_text += " "
                continue
            alphabet_place = alphabet.index(letter) 
            coded_letter_index = alphabet_place + password 
            if coded_letter_index >= 25:    #Safety for if coded letter is >25 runs it all the way back to A
                coded_letter_index = coded_letter_index%26
            coded_letter = alphabet[coded_letter_index]    #Finds coded letter
            code_text += coded_letter                #Joins Strings
        return code_text






    def decode(self, coded_text, password):
        alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


        decoded_text = ""
        for letter in coded_text:            #Loop to decode message
            if letter == " ":
                decoded_text += " "
                continue                         
            alphabet_place = alphabet.index(letter) 
            decoded_letter_index = alphabet_place + (26-password)
            if decoded_letter_index > 25:
                decoded_letter_index = decoded_letter_index%26
            decoded_letter = alphabet[decoded_letter_index]    #Finds plaintext letter
            decoded_text += decoded_letter                #Joins Strings
        return decoded_text

