""" This is my collection of attempts at the Python Challenge
http://www.pythonchallenge.com/
"""

def problem1():
    """ http://www.pythonchallenge.com/pc/def/0.html
    Answer = 274877906944
    """
    print(2**38)

def problem2():
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


def problem3():
    """ http://www.pythonchallenge.com/pc/def/ocr.html
    recognize the characters. maybe they are in the book, 
    but MAYBE they are in the page source.
    """




if __name__ == '__main__':
    problem2()
