from infi_temp_pad_cipher import infi_temp_pad
itp = infi_temp_pad()
running = True
choice = int(input("Encode[1] Decode[2] Quit[3]: "))


while running == True:
    if choice == 1:
        string = input("Message to encode:")
        shift_seed = int(input("Shift Seed: "))
        string = itp.infi_temp_pad_sanitize(string)
        print(itp.infi_temp_pad_encode(string,shift_seed))
        choice = int(input("Encode[1] Decode[2] Quit[3]: "))

    elif choice == 2:
        string = input("Message to decode:")
        shift_seed = int(input("Shift Seed: "))
        string = itp.infi_temp_pad_sanitize(string)
        print(itp.infi_temp_pad_decode(string,shift_seed))
        choice = int(input("Encode[1] Decode[2] Quit[3]: "))

    elif choice == 3:
        running = False
        break
    else:
        print("Please Enter 1, 2 or 3")
        choice = int(input("Encode[1] Decode[2] Quit[3]: "))

