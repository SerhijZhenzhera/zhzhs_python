'''
Task 3. TV controller
Create a simple prototype of a TV controller in Python. It’ll use the following commands:
    first_channel() - turns on the first channel from the list.
    last_channel() - turns on the last channel from the list.
    turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
    next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
    previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
    current_channel() - returns the name of the current channel.
    is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes", if the channel N or 'name' exists in the list,
        or "No" - in the other case.
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
    channel = channels[0]

    def __init__(self, ch):
        self.choose_channel = ch

    def first_channel():
        channel = channels[0]
        TVController.channel = channel  # controller = TVController.channel ?
        return channel

    def last_channel():
        channel = channels[len(channels)-1]
        TVController.channel = channel
        return channel

    def next_channel():
        if not TVController.channel == channels[len(channels)-1]:
            channel = channels[channels.index(TVController.channel)+1]
            TVController.channel = channel
            return channel
        else:
            channel = channels[0]
            TVController.channel = channel
            return channel

    def previous_channel():
        if not TVController.channel == channels[0]:
            channel = channels[channels.index(TVController.channel)-1]
            TVController.channel = channel
            return channel
        else:
            channel = channels[len(channels)-1]
            TVController.channel = channel
            return channel

    def current_channel():
        channel = TVController.channel
        return channel

    def turn_channel(ch):
        if type(ch) is int:
            if 0 < int(ch) < len(channels):
                channel = channels[ch-1]
                TVController.channel = channel
                return channel
            else:
                print('Choose right number, please')
                channel = TVController.channel
                return channel
        else:
            print('Only numbers, please!')
            channel = TVController.channel
            return channel

    def is_exists(ch):
        if type(ch) is int:
            if 0 < int(ch) < len(channels):
                print('Yes')
                channel = TVController.channel
                return channel
            else:
                print('No')
                channel = TVController.channel
                return channel
        elif type(ch) is str:
            if ch in channels:
                print('Yes')
                channel = TVController.channel
                return channel
            else:
                print('No')
                channel = TVController.channel
                return channel
        else:
            print('No')
            channel = TVController.channel
            return channel


ch1 = TVController.first_channel()
print(ch1)
ch2 = TVController.last_channel()
print(ch2)
ch3 = TVController.next_channel()
print(ch3)
ch4 = TVController.next_channel()
print(ch4)
ch5 = TVController.first_channel()
print(ch5)
ch6 = TVController.previous_channel()
print(ch6)
ch7 = TVController.previous_channel()
print(ch7)
ch8 = TVController.current_channel()
print(ch8)
ch9 = TVController.turn_channel('a')
print(ch9)
ch10 = TVController.turn_channel(7)
print(ch10)
ch11 = TVController.turn_channel(3)
print(ch11)
ch12 = TVController.is_exists(5)
print(ch12)
ch13 = TVController.is_exists(2)
print(ch13)
ch14 = TVController.is_exists('Eurosport')
print(ch14)
ch15 = TVController.is_exists('ICTV')
print(ch15)

'''
---output---
BBC
5 channel
BBC
Discovery
BBC
5 channel
ICTV
ICTV
Only numbers, please!
ICTV
Choose right number, please
ICTV
TV1000
No
TV1000
Yes
TV1000
No
TV1000
Yes
TV1000
'''
