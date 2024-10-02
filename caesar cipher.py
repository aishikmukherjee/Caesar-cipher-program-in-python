import caesar_data

#logo
print(caesar_data.logo)

#===========================>> ENCRYPTION <<===========================
def encode(text, shift_amount):
    encoded_text = ""
    if len(text) == 0:
        print("\nNothing to encode")
    else:
        for letter in text:
# for lower-case alphabets =========================================================================
            if letter in caesar_data.lower_alphabets:
                index_of_letter = caesar_data.lower_alphabets.index(letter)
                result_index = index_of_letter + shift_amount
                if -27 < result_index <26:
                    encoded_text = encoded_text + caesar_data.lower_alphabets[result_index]
                elif result_index > 25:
                    result_index = result_index % 26
                    encoded_text = encoded_text + caesar_data.lower_alphabets[result_index]
                else:
                    result_index = ((result_index * -1) % 26) * -1
                    encoded_text = encoded_text + caesar_data.lower_alphabets[result_index]
#for upper-case alphabets ===========================================================================
            elif letter in caesar_data.upper_alphabets:
                index_of_letter = caesar_data.upper_alphabets.index(letter)
                result_index = index_of_letter + shift_amount
                if -27 < result_index < 26:
                    encoded_text = encoded_text + caesar_data.upper_alphabets[result_index]
                elif result_index > 25:
                    result_index = result_index % 26
                    encoded_text = encoded_text + caesar_data.upper_alphabets[result_index]
                else:
                    result_index = ((result_index * -1) % 26) * -1
                    encoded_text = encoded_text + caesar_data.upper_alphabets[result_index]
#for numbers alphabets ==============================================================================
            elif letter in caesar_data.numbers:
                index_of_letter = caesar_data.numbers.index(letter)
                result_index = index_of_letter + shift_amount
                if -11 < result_index < 10:
                    encoded_text = encoded_text + caesar_data.numbers[result_index]
                elif result_index > 9:
                    result_index = result_index % 10
                    encoded_text = encoded_text + caesar_data.numbers[result_index]
                else:
                    result_index = ((result_index * -1) % 10) * -1
                    encoded_text = encoded_text + caesar_data.numbers[result_index]
#for special characters alphabets ===================================================================
            elif letter in caesar_data.special_characters:
                index_of_letter = caesar_data.special_characters.index(letter)
                result_index = index_of_letter + shift_amount
                if -32 < result_index < 31:
                    encoded_text = encoded_text + caesar_data.special_characters[result_index]
                elif result_index > 31:
                    result_index = result_index % 31
                    encoded_text = encoded_text + caesar_data.special_characters[result_index]
                else:
                    result_index = ((result_index * -1) % 31) * -1
                    encoded_text = encoded_text + caesar_data.special_characters[result_index]
#for unrecognized characters alphabets ==============================================================
            else:
                encoded_text = encoded_text + letter
        print(f"\nEncoded text = {encoded_text}")


#===========================>> DECRYPTION <<===========================
def decode(text, shift_amount):
    decoded_text = ""
    if len(text) == 0:
        print("\nNothing to decode")
    else:
        for letter in text:
# for lower-case alphabets =========================================================================
            if letter in caesar_data.lower_alphabets:
                index_of_letter = caesar_data.lower_alphabets.index(letter)
                result_index = index_of_letter - shift_amount
                if -27 < result_index <26:
                    decoded_text = decoded_text + caesar_data.lower_alphabets[result_index]
                elif result_index > 25:
                    result_index = result_index % 26
                    decoded_text = decoded_text + caesar_data.lower_alphabets[result_index]
                else:
                    result_index = ((result_index * -1) % 26) * -1
                    decoded_text = decoded_text + caesar_data.lower_alphabets[result_index]
#for upper-case alphabets ===========================================================================
            elif letter in caesar_data.upper_alphabets:
                index_of_letter = caesar_data.upper_alphabets.index(letter)
                result_index = index_of_letter - shift_amount
                if -27 < result_index < 26:
                    decoded_text = decoded_text + caesar_data.upper_alphabets[result_index]
                elif result_index > 25:
                    result_index = result_index % 26
                    decoded_text = decoded_text + caesar_data.upper_alphabets[result_index]
                else:
                    result_index = ((result_index * -1) % 26) * -1
                    decoded_text = decoded_text + caesar_data.upper_alphabets[result_index]
#for numbers alphabets ==============================================================================
            elif letter in caesar_data.numbers:
                index_of_letter = caesar_data.numbers.index(letter)
                result_index = index_of_letter - shift_amount
                if -11 < result_index < 10:
                    decoded_text = decoded_text + caesar_data.numbers[result_index]
                elif result_index > 9:
                    result_index = result_index % 10
                    decoded_text = decoded_text + caesar_data.numbers[result_index]
                else:
                    result_index = ((result_index * -1) % 10) * -1
                    decoded_text = decoded_text + caesar_data.numbers[result_index]
#for special characters alphabets ===================================================================
            elif letter in caesar_data.special_characters:
                index_of_letter = caesar_data.special_characters.index(letter)
                result_index = index_of_letter - shift_amount
                if -32 < result_index < 31:
                    decoded_text = decoded_text + caesar_data.special_characters[result_index]
                elif result_index > 31:
                    result_index = result_index % 31
                    decoded_text = decoded_text + caesar_data.special_characters[result_index]
                else:
                    result_index = ((result_index * -1) % 31) * -1
                    decoded_text = decoded_text + caesar_data.special_characters[result_index]
#for unrecognized characters alphabets ==============================================================
            else:
                decoded_text = decoded_text + letter
        print(f"\nDecoded text = {decoded_text}")



while 1 == 1 :
    function = input("\nEnter 'encode' to encrypt message\nEnter 'decode' to decrypt message\n"
                     "Enter anything else to exit program\nEnter Choice: \n").lower()
    if function != 'encode' and function != 'decode':
        print("\nProgram 'Caesar cipher' exited....!!!\n")
        print(caesar_data.credit_of_project)
        exit()
    message = input("Enter your message: \n")
    shift = int(input("Enter shift value: \n"))
    if function == "encode":
        encode(text= message, shift_amount=shift)
    else:
        decode(text= message, shift_amount=shift)

