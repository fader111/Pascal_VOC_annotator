with open('somefile.txt', 'r') as f:
    cont = f.read()
    print(cont)
    if not 'object' in cont:
        print ("ya!!")
    else:
        print("nein!!!")
