def _gen():
    a=0
    while 1:
        a+=1
        b= a+1
        yield a,b
foo = _gen()
print (next(foo))
print (next(foo))
print (next(foo))
