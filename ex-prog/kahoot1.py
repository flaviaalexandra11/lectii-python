###################### Exemple Kahoot ######################

# Variabile. Tipuri de date. Operatori 

a = 3
b = 5
c = a + b
print(c)

x = "7"
y = "12"
z = x + y
print(z)

a = 4
d = a * 3
print(d)

a = 6
b = 2
d = a / b
print(d)

a = 3
d = a % 2
print(d)

# Operatii pe valori boolene.

q = True
w = False
e = q and w
print(e)

q = True
w = True
e = q and w
print(e)

q = True
w = False
e = q or w
print(e)

q = True
y = not q
print(y)

# Instructiunea if. 

a = 2
if a < 2: 
    print ("aici")
else:
    print("acolo")

a = 2
if a < 2: 
    print ("aici")
print("acolo")

a = 5
if a < 5:
    print("nope")
elif a == 5:
    print("yess")
else:
    print("hmm..")

x = "hello"
if x == "hello":
    x = "konnichi wa"
print(x)

a = 1
b = 5
x = 2

if x > a and x < b:
    print("aici 1")

if x > a or x > b: 
    print("aici 2")

if not x > b:
    print("aici 3")