'''
Task 4
Function returns reversed input string
'''

def reverse(input_str):
    if len(input_str) == 0:
        return ''
    return input_str[len(input_str)-1] + reverse(input_str[:len(input_str)-1])
    

if __name__ == '__main__':

    assert reverse("hello") == "olleh"
    assert reverse("o") == "o"
    assert reverse("") == ""
