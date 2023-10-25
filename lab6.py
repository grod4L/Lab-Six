# Gregory Rodriguez, Partner: Angel Perez - Lab 6: Password Encoder and Decoder

# Encodes password by adding 3 to each character and returning the new encoded password.
def encode_password(password):
    enc_password = ''
    for char in password:
        encoded_char = str(int(char) + 3)
        enc_password += encoded_char
    return enc_password


# Decodes password by subtracting 3 from each character and returning the decoded password.
def decode_password(encoded_password):
    d_password = ''
    for char in encoded_password:
        decoded_character = str(int(char) - 3)
        d_password += decoded_character
    return d_password


if __name__ == '__main__':

    menu_option = 0

    while menu_option != 3:

        # Display user menu
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit\n')

        # Prompt user for menu option
        menu_option = int(input('Please enter an option: '))

        # Following branches will encode or decode password based on user menu choice.
        if menu_option == 1:
            original_password = str(input('Please enter your password to encode: '))
            encoded_password = encode_password(original_password)
            print('Your password has been encoded and stored!\n')

        elif menu_option == 2:
            decoded_password = decode_password(encoded_password)
            print(f'The encoded password is {encoded_password}, and the original password is {decoded_password}.\n')
