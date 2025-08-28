from Brannam_Cipher import brannam_cipher
bc = brannam_cipher()
running = True
choice = int(input("Encode[1] Decode[2] Quit[3]: "))


while running == True:
    if choice == 1:
        string = input("Message to encode:")
        shift_seed = int(input("Shift Seed: "))
        string = bc.brannam_sanitize(string)
        print(bc.brannam_encode(string,shift_seed))
        choice = int(input("Encode[1] Decode[2] Quit[3]: "))

    elif choice == 2:
        string = input("Message to encode:")
        shift_seed = int(input("Shift Seed: "))
        string = bc.brannam_sanitize(string)
        print(bc.brannam_decode(string,shift_seed))
        choice = int(input("Encode[1] Decode[2] Quit[3]: "))

    elif choice == 3:
        running = False
        break
    else:
        print("Please Enter 1, 2 or 3")
        choice = int(input("Encode[1] Decode[2] Quit[3]: "))

