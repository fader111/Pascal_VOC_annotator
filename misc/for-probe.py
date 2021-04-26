for i in []:
    print('erer')

a='\\'
with open("misc/test.txt", "r") as f:
    for line in f:
        line_par = line.split('\\') 
        print('line', line_par[-1][:-1])
    a= f.read()
