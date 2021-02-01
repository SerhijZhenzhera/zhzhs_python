'''
You are given a string and two markers (the initial and final). You have to find a substring enclosed between these two markers. But there are a few important conditions:
    The initial and final markers are always different.
    If there is no initial marker, then the first character should be considered the beginning of a string.
    If there is no final marker, then the last character should be considered the ending of a string.
    If the initial and final markers are missing then simply return the whole string.
    If the final marker comes before the initial marker, then return an empty string.
Input: Three arguments. All of them are strings. The second and third arguments are the initial and final markers.
Output: A string.
How it is used: for parsing texts
Precondition: can't be more than one final marker and can't be more than one initial. Marker can't be an empty string  
'''

import unittest

def between_markers_1(text, begin, end):
    if begin in text:
        text_1 = text.split(begin)
        text = text_1[1]
    if end in text:
        text_2 = text.split(end)
        text = text_2[0]
    print(text)
    return text

def between_markers_2(text, begin, end):
    if begin in text:
        text_1 = text.split(begin)
        if end in text_1[0]:
            return ''
        text = text_1[1]
    if end in text:
        text_2 = text.split(end)
        text = text_2[0]
    print(text)
    return text

class MarkersTestCase(unittest.TestCase):

    def test_markers(self):
        m_1 = between_markers_1('What is >apple<', '>', '<')
        m_2 = between_markers_1('<head><title>My new site</title></head>', '<title>', '</title>')
        m_3 = between_markers_1('No[/b] hi', '[b]', '[/b]')
        m_4 = between_markers_1('No [b]hi', '[b]', '[/b]')
        m_5 = between_markers_1('No hi', '[b]', '[/b]')
        m_6 = between_markers_1('No <hi>', '>', '<')
        # m_7 = between_markers_1('What <is> apple', '>', '<')
        self.assertEqual(m_1, 'apple')
        self.assertEqual(m_2, 'My new site')
        self.assertEqual(m_3, 'No')
        self.assertEqual(m_4, 'hi')
        self.assertEqual(m_5, 'No hi')
        self.assertEqual(m_6, '')
        # self.assertEqual(m_7, '')
        m_8 = between_markers_2('What is >apple<', '>', '<')
        m_9 = between_markers_2('<head><title>My new site</title></head>', '<title>', '</title>')
        m_10 = between_markers_2('No[/b] hi', '[b]', '[/b]')
        m_11 = between_markers_2('No [b]hi', '[b]', '[/b]')
        m_12 = between_markers_2('No hi', '[b]', '[/b]')
        m_13 = between_markers_2('No <hi>', '>', '<')
        m_14 = between_markers_2('What <is> apple', '>', '<')
        self.assertEqual(m_8, 'apple')
        self.assertEqual(m_9, 'My new site')
        self.assertEqual(m_10, 'No')
        self.assertEqual(m_11, 'hi')
        self.assertEqual(m_12, 'No hi')
        self.assertEqual(m_13, '')
        self.assertEqual(m_14, '')

unittest.main()        

'''
---output---1---
apple
My new site
No
hi
No hi

 apple
F
======================================================================
FAIL: test_markers (__main__.MarkersTestCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "r:\Beetroot\Python\17\17a_assert_between_markers.py", line 54, in test_markers
    self.assertEqual(m_7, '')
AssertionError: ' apple' != ''
-  apple
+


----------------------------------------------------------------------
Ran 1 test in 0.002s

FAILED (failures=1)
---output---2---(without 7)
apple
My new site
No
hi
No hi

apple
My new site
No
hi
No hi
.
----------------------------------------------------------------------
Ran 1 test in 0.002s

OK
'''
