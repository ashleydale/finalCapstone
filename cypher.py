# takes a single character as input and returns a new character that is 15 positions ahead of the input character in the ASCII table
def encode_char(char):
    return chr(ord(char)+15)


print("Enter a message:\n")
message = input()
encoded_message = []

# function to convert the string into a list of characters.
for c in list(message):
    if c.isalnum():
        #function is called to encode the character and the encoded character is appended
        encoded_message.append(encode_char(c))
    else:
        encoded_message.append(c)
# After the loop finishes, encoded_message is joined back into a single string
encoded_message = "".join(encoded_message)

print("\n" + encoded_message)
