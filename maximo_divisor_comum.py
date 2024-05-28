def pede_numero():
    num = int(input("Digite um número natural maior que zero: "))
    if num > 0:
        return num
    else:
        return "Número inválido!"

def pega_mdc(lista_divisores):
    comuns = set(lista_divisores[0])
    for lista in lista_divisores[1:]:
        comuns.intersection_update(lista)
    nova_lista = list(comuns)
    nova_lista.sort()
    return nova_lista[-1]

def maximo_divisor_comum():
    repetir = True
    numeros = []
    lista_divisores = []
    while repetir:
        numeros.append(pede_numero())
        escolha = str(input("Deseja adicionar outro número? [S/N]: "))
        while escolha == "S" or escolha == "s":
            numeros.append(pede_numero())
            escolha = str(input("Deseja adicionar outro número? [S/N]: "))
        repetir = False
    numeros.sort()
    for numero in numeros:
        contador = 1
        divisores = []
        while contador <= numero:
            if numero % contador == 0:
                divisores.append(numero//contador)
                contador += 1
            else:
                contador += 1
        divisores.reverse()
        lista_divisores.append(divisores)
    if len(lista_divisores) > 1:
        for lista in lista_divisores:
            print(lista)
        print("O Máximo Divisor Comum é: " + str(pega_mdc(lista_divisores)))
    else:
        print(lista_divisores[0])
        

maximo_divisor_comum()
