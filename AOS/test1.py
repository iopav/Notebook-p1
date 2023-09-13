
#[0*m,1*x,2*x,3*x]
print([m(1) for m in num()])
def num():
    return [lambda x:i*x for i in range(4)]