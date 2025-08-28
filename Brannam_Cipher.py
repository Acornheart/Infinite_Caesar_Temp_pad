from Caesar import caesar
import decimal



class brannam_cipher:
    def __init__(self):
        pass
    def brannam_encode(self,string,shift_seed):

        decimal.getcontext().prec = len(string) + 10
        cipher = caesar()
        shift_setup = decimal.Decimal(shift_seed)
        sqrt_shift = shift_setup.sqrt()
        sqrt_shift_string = str(sqrt_shift)
        sqrt_shift_string = sqrt_shift_string.replace(".","")
        new_string = ""
        for i,letter in enumerate(string):
    
            shift = sqrt_shift_string[i]
            shift = int(shift)
            new_letter = cipher.encode(letter,shift)
            new_string += new_letter
        return new_string
    

    def brannam_decode(self,string,shift_seed):

        decimal.getcontext().prec = len(string) + 10
        cipher = caesar()
        shift_setup = decimal.Decimal(shift_seed)
        sqrt_shift = shift_setup.sqrt()
        sqrt_shift_string = str(sqrt_shift)
        sqrt_shift_string = sqrt_shift_string.replace(".","")
        new_string = ""
        for i,letter in enumerate(string):
    
            shift = sqrt_shift_string[i]
            shift = int(shift)
            new_letter = cipher.decode(letter,shift)
            new_string += new_letter
        return new_string
    
    def brannam_sanitize(self, string):
        string = str(string)
        string = string.lower()
        string = string.replace(" ", "")
        return string