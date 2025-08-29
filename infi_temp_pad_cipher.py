from Caesar import caesar
import decimal



class infi_temp_pad:             #class to call later in running loop
    def __init__(self):
        pass


    def infi_temp_pad_encode(self,string,shift_seed):  #function to encode with that generate a new shift key baed off an irration number

        decimal.getcontext().prec = len(string) + 10
        cipher = caesar()
        shift_setup = decimal.Decimal(shift_seed)
        sqrt_shift = shift_setup.sqrt()            #Generates irrational number
        sqrt_shift_string = str(sqrt_shift)
        sqrt_shift_string = sqrt_shift_string.replace(".","")
        new_string = ""
        for i,letter in enumerate(string):
    
            shift = sqrt_shift_string[i]
            shift = int(shift)
            new_letter = cipher.encode(letter,shift)    #shifts using slice of number
            new_string += new_letter
        return new_string
    

    def infi_temp_pad_decode(self,string,shift_seed):     #function to decode with that generate a new shift key based off an irratational number
        decimal.getcontext().prec = len(string) + 10
        cipher = caesar()
        shift_setup = decimal.Decimal(shift_seed)   
        sqrt_shift = shift_setup.sqrt()          #generates irrational number
        sqrt_shift_string = str(sqrt_shift)
        sqrt_shift_string = sqrt_shift_string.replace(".","")  
        new_string = ""
        for i,letter in enumerate(string):            #generates number
    
            shift = sqrt_shift_string[i]
            shift = int(shift)
            new_letter = cipher.decode(letter,shift) #shifts using number
            new_string += new_letter
        return new_string
    
    def infi_temp_pad_sanitize(self, string):
        string = str(string)
        string = string.lower()
        string = string.replace(" ", "")

        return string
