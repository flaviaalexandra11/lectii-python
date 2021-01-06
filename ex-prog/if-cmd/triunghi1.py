from math import *

a = int(input("Introduceti lungimea primei laturi: "))
b = int(input("Introduceti lungimea celei de a doua laturi: "))
c = int(input("Introduceti lungimea celei de a treia laturi: "))

# daca suma a 2 laturi este mai mare decat a cealalta
# => laturile pot forma un triunghi
if a + b > c:
    if b + c > a:
        if c + a > b:
            # echilateral => toate laturile egale
            if a == b == c:
                print("Triunghi Echilateral")
            # isoscel => 2 laturi egale
            elif a == b or b == c or a == c:
                print("Triunghi Isoscel")
            # dreptunghic => Pitagora
            elif a == sqrt(pow(b, 2) + pow(c, 2)) or\
                    b == sqrt(pow(a, 2) + pow(c, 2)) or\
                    c == sqrt(pow(a, 2) + pow(b, 2)):
                print("Triunghi Dreptunghic")
            # daca nu se incadreaza in nicio categorie
            # => triunghi oarecare
            else:
                print("Triunghi Oarecare")
else:
    print("Laturile nu pot forma un triunghi")