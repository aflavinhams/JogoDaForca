# Ana Flávia Martins dos Santos
# O programa a seguir implementa um Jogo da Forca, onde você deve advinhar a palavra secreta

import random
# Vetor com as palavras que serão randomizadas
print('Bem-vindo ao Jogo da Forca!')
print('Tema: animais')
print('Tenha um bom jogo! :)')

palavras = ["camelo", "cavalo", "ovelha", "coelho", "girafa", "jacaré", "macaco"]

# Randomização da palavra secreta
indice = random.randint(0, 4)
palavra = palavras[indice]
#print(f'Palavra secreta: {palavra}')

# Criação dos vetores com as letras das palavras
camelo = ['c', 'a', 'm', 'e', 'l', 'o']
cavalo = ['c', 'a', 'v', 'a', 'l', 'o']
ovelha = ['o', 'v', 'e', 'l', 'h', 'a']
coelho = ['c', 'o', 'e', 'l', 'h', 'o']
girafa = ['g', 'i', 'r', 'a', 'f', 'a']
jacare = ['j', 'a', 'c', 'a', 'r', 'e']
macaco = ['m', 'a', 'c', 'a', 'c', 'o']

# Criação dos vetores da palavra secreta e da resposta
vetorPalavra = [0] * 6
vetorResposta = ['_'] * 6

# Inicializando a variável tentativas em 8
tentativas = 8

# Bloco while para que a pessoa continue jogando enquanto não esgotar as tentativas
while tentativas > 0 and vetorResposta != vetorPalavra:

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
    elif palavra == 'jacaré':
        vetorPalavra = jacare
    elif palavra == 'macaco':
        vetorPalavra = macaco


    teste = 0
    print(f'Tentativas restantes: {tentativas}')
    letra = input("Digite uma letra: ")
    print(' ')
    for i in range(len(vetorPalavra)):
        if letra == vetorPalavra[i]:
            vetorResposta[i] = vetorPalavra[i]

        elif letra != vetorPalavra[i]:
            teste += 1
        if teste == 6:
            print('A letra digitada não existe')
            print(' ')
            tentativas -= 1

        if vetorResposta == vetorPalavra:
            print('Parabéns! Você acertou a palavra secreta. ')
            break

if tentativas == 0:
    print('Suas tentativas acabaram! :(')

