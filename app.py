from palavras import palavras
from estagios import estagios
import random

#selecionar a palavra
def selecionar_palavra():
    palavra = random.choice(palavras)
    return palavra.upper()

def exibir_forca(tentativas):
    return estagios[tentativas]


#iniciar jogo
def jogar(palavra):
    palavra_a_completar = "_" * len(palavra)
    advinhou = False
    letras_usadas = []
    palavras_usadas = []
    tentativas = 4

    print(palavra)
    print(palavra_a_completar)

    #boas vindas
    print("Vamos jogar!!")
    print(exibir_forca(tentativas))
    print("Esta é a palavra: %s" % palavra_a_completar)


    while not advinhou and tentativas > 0:
        tentativa = input("Digite uma palavra ou letra para continuar: ").upper()

        print(tentativa)

        if len(tentativa) == 1 and tentativa.isalpha():

            if tentativa in letras_usadas:
                print("Voce ja usou esta letra %s <==" % tentativa)

            elif tentativa not in palavra:
                print("A letra %s <== nao esta na palavra " % tentativa)
                tentativas -= 1
                letras_usadas.append(tentativa)

            else:
                print("Você acertou letra %s está na palavra" % tentativa)
                letras_usadas.append(tentativa)
                palavra_lista = list(palavra_a_completar)

                #print(palavra_a_completar)

                indices = [i for i, letra in enumerate(palavra) if letra == tentativa]

                for indice in indices:
                    palavra_lista[indice] = tentativa

                palavra_a_completar = "".join(palavra_lista)

                if "_" not in palavra_a_completar:
                    advinhou = True

        elif len(tentativa) == len(palavra) and tentativa.isalpha():

            if tentativa in palavras_usadas:
                print("você ja usou está palavra %s" % tentativa)
            elif tentativa != palavra:
                print("A palavra %s está incorreta"% tentativa)
                tentativas -= 1
                palavras_usadas.append(tentativa)
            else:
                advinhou = True
                palavra_a_completar = palavra

        else:
            print("Errado, tente novamente!!!")

        print(exibir_forca(tentativas))
        print(palavra_a_completar)

    if advinhou:
        print("Parabens, Voce acertou a palavra")
    else:
        print("Acabaram as tentativas. A palavra era: %s" % palavra)

def iniciar():
    palavra = selecionar_palavra()
    jogar(palavra)

    while input("jogar novamente?? (S/N)").upper() == 'S':
        palavra = selecionar_palavra()
        jogar(palavra)

iniciar()