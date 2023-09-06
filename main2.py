import random

def adivinhe(x): #--Parametro--
    numero_aleatorio = random.randint(1, x)
    adivinhe = 0
    tentativas = 0

    while adivinhe != numero_aleatorio and tentativas < 3:
        adivinhe = int(input(f'Adivinhe o número entre 1 e {x}: '))
        print(adivinhe)
        if adivinhe < numero_aleatorio:
            print(f'O número secreto é mais alto que {adivinhe}') #--Número é mais alto--
        elif adivinhe > numero_aleatorio:
            print(f'O número secreto é mais baixo que {adivinhe}') #--Númeor é mais baixo--
        tentativas += 1

        if (adivinhe == numero_aleatorio):
            print(f'Parabens guria, acertou o número: {numero_aleatorio}')
        elif tentativas == 3:
            print(f'Voce não acertou em {tentativas} tentativas')        

adivinhe(10)