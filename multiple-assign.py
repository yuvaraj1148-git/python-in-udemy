# it is normal assignment
a = 1
print(a)
print(id(a))

# multiple assignment

a = b = c = 1
print(a,b,c)
print(id(a))
print(id(b))
print(id(c))

# also assign like this 
a,b,c = 1,1,1
print(a,b,c)
print(id(a))
print(id(b))
print(id(c))

# note onething all the id are also because if you assign a same value to all variable python store the value as memory to the all same variable

a = 1
b = 2
c = 3

print(id(a))
print(id(b))
print(id(c))