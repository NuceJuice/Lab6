import sys


# Parter: Julian Garcia

def encode(password):
    encodedString = ""
    for i in password:
        encodedString += str(int(i) + 3)
    print("Your password has been encoded and stored!")
    print()
    return encodedString


def decode(password):
    decodedString = ''
    for i in password:
        decodedString += str(int(i) - 3)
    return decodedString


def main():
    encoded = None

    while True:
        print("Menu")
        print("---------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()

        menu_selection = int(input("Please enter an option: "))
        if menu_selection == 1:
            password = input("Please enter your password to encode: ")
            encoded = encode(password)

        elif menu_selection == 2:
            decoded = decode(encoded)
            print(f'The encoded password is {encoded}, and the original password is {decoded}.')
            print('')


        elif menu_selection == 3:
            sys.exit()


if __name__ == '__main__':
    main()
