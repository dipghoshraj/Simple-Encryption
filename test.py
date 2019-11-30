from algorithem import Algo

m = Algo()

x=  m.encrypt(keyword= 'DGp')
print(x)

y= m.match(keyword= x, validator='DGp')

print(y)
