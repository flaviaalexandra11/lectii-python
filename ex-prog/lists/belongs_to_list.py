'''
    Belongs-To-List.
    Se da lista: 1, 22, 3, 19, 2, 18, 16, 5, 8, 16, 4, 13, 34, 11, 7.
    Să se citească un număr de la tastatură, să se verifice dacă acesta aparține listei și să se afișeze un mesaj corespunzător.
'''

my_list = [1, 22, 3, 19, 2, 18, 16, 5, 8, 16, 4, 13, 34, 11, 7]
my_num = int(input('Numarul de cautat este: '))
found = False

for i in range(0, len(my_list)):
    if my_num == my_list[i]:
        print('Gasit pe pozitia {}'.format(i))
        found = True

if not found:
    print('Nu l-am gasit :(')

