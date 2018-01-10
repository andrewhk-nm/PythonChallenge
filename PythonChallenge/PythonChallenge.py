""" This is my collection of attempts at the Python Challenge
http://www.pythonchallenge.com/
"""

import os
import string
from collections import namedtuple

class HelperFunctions:
    """ Store my helper functions here for easier testing and re-use.
    """
    def get_char_count(filename):
        """ Wrapper for the problem2 solution.
        Takes the filename of a text file, and returns a dictionary. 
        The keys are the character and the value is the character count.
        """
        return problem2(filename, print_debug_info=True)

    def gen_char_neighbor(filename):
        """ take a filename of a text file in block format.
        generates the neighbors for the next char.
        returns dict: {char: [1, 2, 3, 4, 6, 7, 8, 9] where:
        123
        456
        789
        """
        a_list = list()
        with open(filename, encoding='utf-8') as a_file:
            for a_line in a_file:
                a_list.append(a_line.rstrip())

        #print('a_list={}'.format(a_list))

        # Start at line 2 char 2, end at the 2nd to last line, 2nd to last char
        for line in range(1, len(a_list) - 1):
            for char in range(1, len(a_list[line]) - 1):
                #print('a_list[{}][{}] = {}'.format(line, char, a_list[line][char]))
                # So for each letter in the block, check each surrounding letter, and count the Big letters.
                #     (x-1)-row_length  x-row_length  (x+1)-row_length 
                #     (x-1)             x             (x+1)
                #     (x-1)+row_length  x+row_length  (x+1)+row_length 
                # If Count(outsides) = 3 big letters then success
                Line_char = namedtuple('Line_char', 'line char')
                line_char_1 = Line_char(line - 1, char - 1)
                line_char_2 = Line_char(line - 1, char)
                line_char_3 = Line_char(line - 1, char + 1)
                line_char_4 = Line_char(line, char - 1)
                line_char_6 = Line_char(line, char + 1)
                line_char_7 = Line_char(line + 1, char - 1)
                line_char_8 = Line_char(line + 1, char)
                line_char_9 = Line_char(line + 1, char + 1)
                line_char_all = ''.join([a_list[line_char_1.line][line_char_1.char],
                                        a_list[line_char_2.line][line_char_2.char],
                                        a_list[line_char_3.line][line_char_3.char],
                                        a_list[line_char_4.line][line_char_4.char],
                                        a_list[line_char_6.line][line_char_6.char],
                                        a_list[line_char_7.line][line_char_7.char],
                                        a_list[line_char_8.line][line_char_8.char],
                                        a_list[line_char_9.line][line_char_9.char],
                                        ])
                                
                yield {a_list[line][char], line_char_all}


        #yield {1:2}

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


def problem2(filename='problem2_mess_below.txt', print_debug_info=True):
    """ takes the file name and counts the characters.
    Returns a dictionary of the character and the count.
    Allows an optional parameter, print_debug_info, that 
    if True will print extra debug info, if False it won't.

    http://www.pythonchallenge.com/pc/def/ocr.html
    recognize the characters. maybe they are in the book, 
    but MAYBE they are in the page source.
    Answer = "equality"
    """

    # Create an empty dictionary to store the counts of characters
    char_counter = dict()
    with open(filename, encoding='utf-8') as p2_file:
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

    if print_debug_info:
        print('char_counter: {}'.format(char_counter))

        # Print the rare (Unique) characters only
        print('Print the rare (Unique) characters only.')
        for k, v in char_counter.items():
            if v == 1:
                print(k)

    return char_counter

def problem3():
    """ http://www.pythonchallenge.com/pc/def/equality.html
        One small letter, surrounded by EXACTLY three big bodyguards on each of its sides.
    """

    print("entering #3")

    #char_dict = HelperFunctions.get_char_count('problem3_source_mess.txt')
    

    #print('char_dict = \n{}'.format(char_dict))
    #print('char_dict, keys only = {}'.format(char_dict.keys()))
    #a_list = list(char_dict.keys())
    #a_list.sort()
    #print('a_list = {}'.format(a_list)) # Contains all letters a-z and A-Z
    # I think the answer will be this:
    # BBB
    # axa
    # aaa
    # or
    # aBB
    # axB
    # aaa
    # etc.
    # So for each letter in the block, check each surrounding letter, and count the Big letters.
    #     (x-1)-row_length  x-row_length  (x+1)-row_length 
    #     (x-1)             x             (x+1)
    #     (x-1)+row_length  x+row_length  (x+1)+row_length 
    # If Count(outsides) = 3 big letters then success

    gen_neighbors_dict = HelperFunctions.gen_char_neighbor('problem3_source_mess.txt')
    #neighbors_dict = gen_neighbors_dict()
    for k, v in gen_neighbors_dict:
        print('k={}, v={}'.format(k,v))
        if string.ascii_uppercase.find(k) == -1:
            caps = v.strip(string.ascii_lowercase)

    a_test = ['A', 'B', 'c']
    str.strip(string.ascii_uppercase)
    string.ascii_uppercase




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
    

if __name__ == '__main__':
    print("__main__")
    problem3()
