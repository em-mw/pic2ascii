with open('s', 'w+') as o:
    o.write('s')
    o.seek(0)
    print(o.read())