'''
Task 1. Method overloading

Create a class method named `validate`, which should be called from the `__init__` method to validate parameter email, passed to the constructor.
The logic inside the `validate` method could be to check if the passed email parameter is a valid email string
'''


class Address():
    def __init__(self, e_mail):
        self.e_mail = e_mail

    @property
    def validate(self):
        e_mail = self.e_mail
        if not type(e_mail) == str:
            print('Not a string!')
            return False
        elif not e_mail.count('@') == 1:
            print('there should be one and only one "@"')
            return False
        else:
            at = e_mail.find('@')
            local_part = e_mail[:at]
            domain_part = e_mail[at+1:]
            quoted = ''
            if len(local_part) > 64:
                print('too long!')
                return False
            elif '_' in domain_part:
                print('not valid!')
                return False
            elif '"' in domain_part:
                print('not valid!')
                return False
            elif '"' in local_part:
                if not local_part.count('"') == 2:
                    print('not valid!')
                    return False
                else:
                    q_1 = local_part.find('"')
                    temp = local_part.replace('"', 't', 1)
                    q_2 = temp.find('"')
                    quoted = local_part[q_1+1: q_2]
            if '(' and ')' and ',' and ':' and ';' and '<' and '>' and '[' and '\\' and ']' and '..' in e_mail:
                if not '(' and ')' and ',' and ':' and ';' and '<' and '>' and '[' and '\\' and ']' and '..' in quoted:
                    print('not valid!')
                    return False
            else:
                print('e_mail verified!')
                return e_mail


if __name__ == "__main__":
    a1 = Address('shvjed@ukr.net')
    a2 = Address(0)
    a3 = Address('Abc.example.com')
    a4 = Address('A@b@c@example.com')
    a5 = Address('a"b(c)d,e:f;g<h>i[j\k]l@example.com')
    a6 = Address('this is"not\allowed@example.com')
    a7 = Address('this\ still\"not\\allowed@example.com')
    a8 = Address(
        '1234567890123456789012345678901234567890123456789012345678901234+x@example.com')
    a9 = Address(
        'i_like_underscore@but_its_not_allowed_in_this_part.example.com')

    # ??? quoted strings must be dot separated or the only element making up the local-part
    q1 = Address('just"not"right@example.com')


print(a1.validate)
print(a2.validate)
print(a3.validate)
print(a4.validate)
print(a5.validate)
print(a6.validate)
print(a7.validate)
print(a8.validate)
print(a9.validate)
print(q1.validate)


'''
---output---
shvjed@ukr.net
Not a string!
False
there should be one and only one "@"
False
there should be one and only one "@"
False
not valid!
False
not valid!
False
not valid!
False
too long!
False
not valid!
False
e_mail verified!
just"not"right@example.com
'''
