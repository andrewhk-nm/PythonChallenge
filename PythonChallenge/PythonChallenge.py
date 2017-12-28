""" This is my collection of attempts at the Python Challenge
http://www.pythonchallenge.com/
"""

import os

def problem0():
    """ http://www.pythonchallenge.com/pc/def/0.html
    Answer = 274877906944
    """
    print(2**38)

def problem1():
    """ http://www.pythonchallenge.com/pc/def/map.html
    everybody thinks twice before solving this.

    g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.
    Answer = i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url.
    Answer = "map.html" -> "ocr.html"
    
    """
    encoded = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."


    # 'abcdefghijklmnopqrstuvwxyz'

    # k -> m
    # 'abcdefghijklmnopqrstuvwxyz'
    # 'cdefghijklmnopqrstuvwxyzab'
    k_to_m_dict = str.maketrans('abcdefghijklmnopqrstuvwxyz', 'cdefghijklmnopqrstuvwxyzab')

    print(encoded.translate(k_to_m_dict))
    print('http://www.pythonchallenge.com/pc/def/map.html'.translate(k_to_m_dict))


def problem2():
    """ http://www.pythonchallenge.com/pc/def/ocr.html
    recognize the characters. maybe they are in the book, 
    but MAYBE they are in the page source.
    Answer = "equality"
    """

    # Create an empty dictionary to store the counts of characters
    char_counter = dict()
    with open('problem2_mess_below.txt', encoding='utf-8') as p2_file:
        # I want to read the file character by character but I can't really figure out how.
        for p2_line in p2_file:
            # I can't figure out how to iterate through the stringgnngngngngngngn 
            for char_key in p2_line:
                try:
                    # If there is already a key counting the characters, add to it.
                    char_counter[char_key] += 1
                except KeyError:
                    # Key does not yet exist, add it with an inital count of 1
                    char_counter[char_key] = 1

    print(char_counter)

    # Print the rare (Unique) characters only
    print('Print the rare (Unique) characters only.')
    for k, v in char_counter.items():
        if v == 1:
            print(k)

def problem2_wiki():
    """ This problem is "Full solution, get source & open answer page
    It doesn't work because I think it was written for Python2?
    """

    from string import ascii_letters
    import re, urllib2, webbrowser as wb
    wb.open('http://www.pythonchallenge.com/pc/def/%s.html' %
        ''.join(chr for chr in
        re.findall(chr,
        urllib2.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html')
        .read(), re.S)[1] if chr in ascii_letters))

   

def problem_test():
    """ Trying to see if I can get the webbrowser library to work. It will work in the Python shell, but not here...
    """
    import webbrowser as wb

    wb.open_new_tab('http://www.pythonchallenge.com/pc/def/ocr.html')
    

def problem3():
    """ http://www.pythonchallenge.com/pc/def/equality.html
    Not started yet!
    """

if __name__ == '__main__':
    problem_test
