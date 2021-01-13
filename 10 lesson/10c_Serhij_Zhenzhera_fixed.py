'''
Task 3. TV controller
Create a simple prototype of a TV controller in Python. It’ll use the following commands:
    first_channel() - turns on the first channel from the list.
    last_channel() - turns on the last channel from the list.
    turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
    next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
    previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
    current_channel() - returns the name of the current channel.
    is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes",
        if the channel N or 'name' exists in the list, or "No" - in the other case.
The default channel turned on before all commands is №1.
Your task is to create the TVController class and methods described above.
---
CHANNELS = ["BBC", "Discovery", "TV1000"]

 class TVController:

pass

 controller = TVController(CHANNELS)
'''


channels = ["BBC", "Discovery", "TV1000", "ICTV", "5 channel"]


class TVController:
    def __init__(self, ch):
        self.position = 0
        self.choose_channel = ch

    def first_channel(self):
        self.position = 0
        return self.choose_channel[self.position]

    def last_channel(self):
        self.position = len(self.choose_channel)-1
        return self.choose_channel[self.position]

    def next_channel(self):
        if not self.position == len(self.choose_channel)-1:
            self.position += 1
            return self.choose_channel[self.position]
        else:
            self.position = 0
            return self.choose_channel[self.position]

    def previous_channel(self):
        if not self.position == 0:
            self.position -= 1
            return self.choose_channel[self.position]
        else:
            self.position = len(self.choose_channel)-1
            return self.choose_channel[self.position]

    def current_channel(self):
        return channels[self.position]

    def turn_channel(self, ch):
        if ch in range(len(self.choose_channel)):
            self.position = ch
        return self.choose_channel[self.position]          
        
    def is_exists(self, ch):
        if ch in range(len(self.choose_channel)) or ch in self.choose_channel:
            return 'Yes'
        return 'No'

if __name__ == "__main__":
    ch1 = TVController(['1', '2', '3', '4', '5'])
    print(ch1.first_channel())
    print(ch1.last_channel())
    print(ch1.next_channel())
    print(ch1.next_channel())
    print(ch1.first_channel())
    print(ch1.previous_channel())
    print(ch1.previous_channel())
    print(ch1.current_channel())
    print(ch1.turn_channel('a'))
    print(ch1.turn_channel(7))
    print(ch1.turn_channel(3))
    print(ch1.is_exists(5))
    print(ch1.is_exists(2))
    print(ch1.is_exists('Eurosport'))
    print(ch1.is_exists('ICTV'))

    ch2 = TVController(['a', 'b', 'c', 'd', 'e'])
    print(ch2.last_channel())
    print(ch2.previous_channel())
    print(ch2.next_channel())
    print(ch2.first_channel())
    print(ch2.current_channel())
    print(ch2.turn_channel('1'))
    print(ch2.turn_channel('f'))
    print(ch2.turn_channel('c'))
    print(ch2.is_exists(5))
    print(ch2.is_exists('d'))
    print(ch2.is_exists('Discovery'))
    print(ch2.is_exists('TV1000'))



'''
---output---
1
5
1
2
1
5
4
ICTV
4
4
4
No
Yes
No
No
e
d
e
a
BBC
a
a
a
No
Yes
No
No
'''
