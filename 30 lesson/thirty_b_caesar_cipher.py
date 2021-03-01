'''
Task 2
Extend the echo server, which returns to client the data, encrypted using the Caesar cipher algorithm by a specific key obtained from the client
'''


def cipher_encrypt(plain_text, key):  # The Encryption Function
    encrypted = ""
    for c in plain_text:
        if c.isupper():  # check if it's an uppercase character
            c_index = ord(c) - ord('A')
            # shift the current character by key positions
            c_shifted = (c_index + key) % 26 + ord('A')
            c_new = chr(c_shifted)
            encrypted += c_new
        elif c.islower():  # check if its a lowecase character
            # subtract the unicode of 'a' to get index in [0-25) range
            c_index = ord(c) - ord('a')
            c_shifted = (c_index + key) % 26 + ord('a')
            c_new = chr(c_shifted)
            encrypted += c_new
        elif c.isdigit():
            # if it's a number,shift its actual value
            c_new = (int(c) + key) % 10
            encrypted += str(c_new)
        else:
            # if its neither alphabetical nor a number, just leave it like that
            encrypted += c
    return encrypted


def cipher_decrypt(ciphertext, key):  # The Decryption Function
    decrypted = ""
    for c in ciphertext:
        if c.isupper():
            c_index = ord(c) - ord('A')
            # shift the current character to left by key positions to get its original position
            c_og_pos = (c_index - key) % 26 + ord('A')
            c_og = chr(c_og_pos)
            decrypted += c_og
        elif c.islower():
            c_index = ord(c) - ord('a')
            c_og_pos = (c_index - key) % 26 + ord('a')
            c_og = chr(c_og_pos)
            decrypted += c_og
        elif c.isdigit():
            # if it's a number,shift its actual value
            c_og = (int(c) - key) % 10
            decrypted += str(c_og)
        else:
            # if its neither alphabetical nor a number, just leave it like that
            decrypted += c
    return decrypted


if __name__ == '__main__':
    plain_text = "Mate, the adventure ride in Canberra was so much fun, We were so drunk we ended up calling 911!"
    ciphertext = cipher_encrypt(plain_text, 4)
    print("Plain text message:\n", plain_text)
    print("Encrypted ciphertext:\n", ciphertext)


'''
---output---
Plain text message:
 Mate, the adventure ride in Canberra was so much fun, We were so drunk we ended up calling 911!
Encrypted ciphertext:
 Qexi, xli ehzirxyvi vmhi mr Gerfivve aew ws qygl jyr, Ai aivi ws hvyro ai irhih yt geppmrk 355!
'''
