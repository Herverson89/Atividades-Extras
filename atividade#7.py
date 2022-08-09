#atividade consiste em contar quantidade de letras em uma frase
frase = str(input('Digite uma frase: ')).lower()
palavra = str(input('Digite uma letra para contar sua quantidade: '))

print('A frase digitada foi {} ela repete a letra {} em {} vezes na frase'.format(frase, palavra, frase.count(palavra)))
