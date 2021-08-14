import os

def isInt(num):
    """
    Finds if a number is an int or a float.
    This is a better version of the "isinstance"
    function in python. This function returns a
    bool value (like the "isinstance" function)
    :param num: The number to check if is a int
    ::returns True if int
    ::returns False if float
    """
    if str(type(num)) == '<class \'int\'>' or str(type(num)) == '<class \'float\'>':
        num = str(num)
        if num.find('.'):
            if len(num) >= 3:
                if num[2].find('0') == int(-1):
                    return False
                else:
                    return True
            else:
                return True
        else:
            return True
    else:
        return None

def isFloat(num):
    """
    Finds if a number is an int or a float.
    This is a better version of the "isinstance"
    function in python. This function returns a
    bool value (like the "isinstance" function)
    :param num: The number to check if is a float
    ::returns False if int
    ::returns True if float
    """
    if str(type(num)) == '<class \'int\'>' or str(type(num)) == '<class \'float\'>':
        num = str(num)
        if num.find('.'):
            if len(num) >= 3:
                if num[2].find('0') == int(-1):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return None

def truncate_utf8_chars(filename, count, ignore_newlines=True):
    """
    Truncates last `count` characters of a text file encoded in UTF-8.
    :param filename: The path to the text file to read
    :param count: Number of UTF-8 characters to remove from the end of the file
    :param ignore_newlines: Set to true, if the newline character at the end of the file should be ignored
    """
    with open(filename, 'rb+') as f:
        last_char = None

        size = os.fstat(f.fileno()).st_size

        offset = 1
        chars = 0
        while offset <= size:
            f.seek(-offset, os.SEEK_END)
            b = ord(f.read(1))

            if ignore_newlines:
                if b == 0x0D or b == 0x0A:
                    offset += 1
                    continue

            if b & 0b10000000 == 0 or b & 0b11000000 == 0b11000000:
                # This is the first byte of a UTF8 character
                chars += 1
                if chars == count:
                    # When `count` number of characters have been found, move current position back
                    # with one byte (to include the byte just checked) and truncate the file
                    f.seek(-1, os.SEEK_CUR)
                    f.truncate()
                    return
            offset += 1
