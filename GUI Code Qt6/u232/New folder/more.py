import os, decimal

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
    def num_to_str(f):
        #create a new context for this task
        ctx = decimal.Context()

        # 30 digits should be enough for everyone :D
        ctx.prec = 30
        
        d1 = ctx.create_decimal(f)
        return format(d1, 'f')
    
    if str(num) == '':
        return False

    for p in range(len(str(num))):
        if not any(c in str(num)[p] for c in '0123456789.'):
            return False
    
    num = num_to_str(num)
    if num.find('.') != int(-1):
        if len(num) >= 2:
            numl = list(num)
            elx = 0
            dolto = int(num.find('.'))
            for qot in numl[:]:
                if qot.find('.') != int(-1) or int(elx) < int(dolto):
                    if int(int(len(numl)) - int(1)) == int(elx):
                        return True
                    else:
                        elx += 1
                        continue
                elif int(elx) > int(dolto):
                    if qot.find('0') == int(-1):
                        return False
                    elif int(int(elx) + int(1)) == len(numl) and str(num[-1]) == str(qot) and qot.find('0') != int(-1):
                        return True                        
                elx += 1
        else:
            return True
    else:
        return True

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
    def num_to_str(f):
        #create a new context for this task
        ctx = decimal.Context()

        # 30 digits should be enough for everyone :D
        ctx.prec = 30
        
        d1 = ctx.create_decimal(f)
        return format(d1, 'f')
    
    if str(num) == '':
        return False

    for p in range(len(str(num))):
        if not any(c in str(num)[p] for c in '0123456789.'):
            return False    
    
    num = num_to_str(num)
    if num.find('.') != int(-1):
        if len(num) >= 2:
            numl = list(num)
            elx = 0
            dolto = int(num.find('.'))
            for qot in numl[:]:
                if qot.find('.') != int(-1) or int(elx) < int(dolto):
                    if int(int(len(numl)) - int(1)) == int(elx):
                        return False
                    else:
                        elx += 1
                        continue
                elif int(elx) > int(dolto):
                    if qot.find('0') == int(-1):
                        return True
                    elif int(int(elx) + int(1)) == len(numl) and str(num[-1]) == str(qot) and qot.find('0') != int(-1):
                        return False                        
                elx += 1
        else:
            return False
    else:
        return False

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
