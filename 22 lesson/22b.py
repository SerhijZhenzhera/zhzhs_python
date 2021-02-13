'''
Task 2
Checks if input string is Palindrome
'''

def is_palindrome(looking_str, index = 0):
    if index >= len(looking_str)//2:
        return True
    if looking_str[index] != looking_str[len(looking_str)-1-index]:
        return False
    return is_palindrome(looking_str, index+1)

    

if __name__ == '__main__':

    assert is_palindrome('mom') == True
    assert is_palindrome('sassas') == True
    assert is_palindrome('o') == True
    assert is_palindrome('mmoommm') == False
    assert is_palindrome('mom!') == False
