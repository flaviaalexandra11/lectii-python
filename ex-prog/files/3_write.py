########################## Exemplu write ##########################

# Deschidem fisierul pentru scriere ("w" - write)
output_file = open("output.txt", "w")

# Scriem nr_linii linii in fisier
nr_linii = 5

for i in range(0, nr_linii):
    output_file.write("Linia {}\n".format(i+1))

# Inchidere fisier
output_file.close()
