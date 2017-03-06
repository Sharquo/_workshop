file = open('text.txt', 'r')


while 1:
    char = file.read(1)
    if not char: break
    for i in char:
        if i.isalpha():
            print(i)

file.close()
