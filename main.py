import random
from os import system, name

def cls():
    _ = system('cls')
    
class Termooo():
    #Metodo construtor, cria um dict vazio para as letras escolhidas e recebe a palavra do jogo
    def __init__(self,palavra):
        self.palavra = palavra
        self.letras_escolhidas = {}
    #Mostra o progresso do jogo         
    def mostra_jogo(self):
        cls()
        tabuleiro = ''
        for numero in range(1,6):
            if numero in self.letras_escolhidas:
                tabuleiro += self.letras_escolhidas[numero]
            else: 
                tabuleiro += '[_]'
        print(tabuleiro)
    #A cada tentativa do jogador: o programa limpa o prompt, verifica se a palavra se encaixa no parametro do jogo
    #   e faz a analise combinatória das letras escolhidas pelo jogador e da palavra do jogo
    def tentativa(self,tentativa):
        if len(tentativa) != 5: #and tentativa in possibilidades
            print("Insira uma palavra com apenas 5 letras!")
            return
        else:
            indice_tentativa = 1
            indice_palavra = 1
            for letra_tenativa in tentativa:
                for letra_palavra in self.palavra:                    
                    if letra_tenativa == letra_palavra and indice_palavra == indice_tentativa:
                        self.letras_escolhidas[letra_tenativa] = indice_palavra
                    elif letra_tenativa == letra_palavra and indice_palavra != indice_tentativa:
                        self.letras_escolhidas[letra_tenativa] = 0
                    elif letra_tenativa != letra_palavra:
                        self.letras_escolhidas[letra_tenativa] = 'x'
                indice_palavra += 1
            indice_tentativa += 1
        mostra_jogo()
    
    def end_game():
        pass