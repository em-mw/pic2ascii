def isInt(num):
    if str(type(num)) == '<class \'int\'>' or str(type(num)) == '<class \'float\'>':
        num = str(num)
        if num.find('.') != int(-1):
            if len(num) >= 2:
                numl = list(num)
                elx = 0
                dolto = int(num.find('.'))
                for qot in numl[:]:
                    if qot.find('.') != int(-1) or int(elx) < int(dolto):
                        elx += 1
                        continue
                    elif int(elx) > int(dolto):
                        if qot.find('0') == int(-1):
                            return True
                    if str(num[-1]) == str(qot) and qot.find('0') != int(-1):
                        return False
                    elx += 1
            else:
                return False
        else:
            return False
    else:
        return False

print(isInt(200.60))
