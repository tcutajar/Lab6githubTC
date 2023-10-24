def main():  # Tyler Cutajar
    menu = True
    password = ""
    
    while menu:
        print(f"\nMenu\n"
              "-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        option = input("\nPlease enter an option: ")

        if option == "1":
            while len(password) != 8:
                password = input("Please enter your password to encode: ")
            en_password = encode(password)
            print("Your password has been encoded and stored!")
        elif option == "2":
            print(f'The encoded password is {en_password}, and the original password is {decode(en_password)}')
        elif option == "3":
            menu = False


def encode(passwrd):
    temp_pswrd = ""
    for i in range(0, len(passwrd)):
        if int(passwrd[i]) >= 7:
            temp_pswrd += str(int(passwrd[i]) + 3)[1:2]

        else:
            temp_pswrd += str(int(passwrd[i]) + 3)
    return temp_pswrd

def decode(en_password):
    dec_passwd = ""
    for i in en_password:
        if int(i) > 2:
            dec_passwd += str(int(i) - 3)
        else:
            dec_passwd += str(int(i) + 7)
    return dec_passwd

if __name__ == '__main__':
    main()
