
################### Ceas ###########################

ora = int(input("Care este ora? "))

if ora > 6 and ora <= 11:
    print("Este dimineata")
elif ora > 11 and ora <= 14:
    print("Este pranz")
elif ora > 14 and ora <= 16:
    print("Este dupa amiaza")
elif ora > 16 and ora <= 20:
    print("Este seara")
elif (ora > 20 and ora <= 24) or (ora >= 0 and ora <= 5):
    print("Este noapte")
else:
    print("Ora introdusa nu exista pe planeta Pamant")