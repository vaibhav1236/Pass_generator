import string
import random
i=int(input("Enter the integer value for your no of characters in password\n"))
v=[]
s = string.ascii_lowercase
u = string.ascii_uppercase
p = string.punctuation
k = string.digits

v.extend(list(s))
v.extend(list(u))
v.extend(list(p))
v.extend(list(k))

random.shuffle(v)

#print("".join(v[0:i]))

#or

print("your password is :")
print("".join(v[0:i]))