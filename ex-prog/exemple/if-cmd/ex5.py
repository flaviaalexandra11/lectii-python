###################### Exemple if-uri imbircate ######################

n = input("Intruduceti n: ")

if n >= 0:
    print("Mai mare sau egal cu zero")
    if n == 0:
        print("Zero")
    else:
        print("Mai mare ca zero")
else:
    print("Mai mic ca zero") 


x = input("Intruduceti x: ")

if x > 10:
    print("Mai mare ca 10, ")
    if x > 20:
        print("si mai mare ca 20!")
    else:
        print("dar nu mai mare ca 20.")