a='''wer'''
print(id(a))
b=a
print(id(b)==id(a)) # True
a='''wsd'''
print(id(b)==id(a)) # False
print(id(a))
print(id(b)) # differs
