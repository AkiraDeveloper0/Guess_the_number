import random

def adivinhe(x): #--Parametro--
    numero_aleatorio = random.randint(1, x)
    adivinhe = 0
    while adivinhe != numero_aleatorio:
        adivinhe = int(input(f'Adivinhe o número entre 1 e {x}: '))
        print(adivinhe)
        if adivinhe < numero_aleatorio:
            print(f'O número secreto é mais alto que {adivinhe}') #--Número é mais alto--
        elif adivinhe > numero_aleatorio:
            print(f'O número secreto é mais baixo que {adivinhe}') #--Númeor é mais baixo--

    print(f'Parabens guria, acertou o número: {numero_aleatorio}')        

adivinhe(10)