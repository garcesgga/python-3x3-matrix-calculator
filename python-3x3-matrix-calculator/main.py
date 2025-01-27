import numpy as matriz

m1 = matriz.array([[1, 2, 3], [2, 1, 3], [3, 2, 1]])
m2 = matriz.array([[3, 2, 1], [3, 1, 2], [1, 2, 3]])

while True:
    menu_leia = int(input("1)Imprima\n2)Soma\n3)Multiplicação\n4)Subtração\nSelecione:"))
    if menu_leia == 1:
        print("Opção imprimir selecionada\n", m1,"\n",m2)
    elif menu_leia == 2:
        calc_1 = matriz.add(m1, m2)
        print("Opção Soma selecionada\n", calc_1)
    elif menu_leia == 3:
        calc_2 = matriz.multiply(m1, m2)
        print("Opção Multiplicação selecionada\n", calc_2)
    elif menu_leia == 4:
        calc_3 = matriz.subtract(m1, m2)
        print("Opção Subtração selecionada\n", calc_3)
    else: break
