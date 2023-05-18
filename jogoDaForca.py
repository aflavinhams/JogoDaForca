# Ana Flávia Martins dos Santos
# O jogo funciona apenas se você digitar as letras na ordem certa :/

import random
# Vetor com as palavras que serão randomizadas
palavras = ["camelo", "cavalo", "ovelha", "coelho", "girafa"]

# Randomização da palavra secreta
indice = random.randint(0, 4)
palavra = palavras[indice]
print(palavra)

# Criação dos vetores com as letras das palavras
camelo = ['c', 'a', 'm', 'e', 'l', 'o']
cavalo = ['c', 'a', 'v', 'a', 'l', 'o']
ovelha = ['o', 'v', 'e', 'l', 'h', 'a']
coelho = ['c', 'o', 'e', 'l', 'h', 'o']
girafa = ['g', 'i', 'r', 'a', 'f', 'a']

# Criação dos vetores da palavra secreta e da resposta
vetorPalavra = [0] * 6
vetorResposta = ['_'] * 6

# Inicializando a variável tentativas em 8
tentativas = 8

# Bloco while para que a pessoa continue jogando enquanto não esgotar as tentativas
while tentativas > 0:
    #print(f'Tentativas restantes: {tentativas}')
    print(f'Palavra: {vetorResposta}')

    #Bloco if - elif para estabelecer o vetorPalavra
    if palavra == 'camelo':
        vetorPalavra = camelo
    elif palavra == 'cavalo':
        vetorPalavra = cavalo
    elif palavra == 'ovelha':
        vetorPalavra = ovelha
    elif palavra == 'coelho':
        vetorPalavra = coelho
    elif palavra == 'girafa':
        vetorPalavra = girafa

    # Bloco for para identificar a letra escolhida pelo usuário
    for i in range(len(vetorPalavra)):

        print(f'Tentativas restantes: {tentativas}')
        letra = input("Digite uma letra: ")
        if letra == vetorPalavra[i]:
            vetorResposta[i] = vetorPalavra[i]
        else:
            print('A letra digitada não existe! ')
            tentativas -= 1
        print(vetorResposta)

        if vetorResposta == vetorPalavra:
            print('Parabéns! Você acertou a palavra secreta. ')
            break
    # print('Parabéns! Você acertou a palavra secreta. ')

if tentativas == 0:
    print('Suas tentativas acabaram! :(')

