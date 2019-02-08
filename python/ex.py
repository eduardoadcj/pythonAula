t = input("Informe um número de 1 a 10\n")

t = int(t)

if t >= 1 and t <= 10:

    x = 1

    print("---------------------")

    while x <= 10:
        print(x,"X",t,"=",t*x)
        x+=1

    print("---------------------")


else:
    print("Valor inválido!")
