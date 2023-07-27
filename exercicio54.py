lista  = []

while True:

    print("Selecione uma opcao")
    escolha_usuario = input("[I]nserir [A]pagar [L]istar: ").lower()

    if escolha_usuario == "i":
        add_lista = input("Valor: ")
        lista.append(add_lista)

    elif escolha_usuario == "l":
        for a, b in enumerate(lista):
            print(a, b)
    elif escolha_usuario == "a":
        indice_str = input("Escolha o indice que deseja apagar: ")

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print("Digite um numero inteiro.")
        except IndexError:
            print("Esse indice nao existe na lista")
        

    
     


