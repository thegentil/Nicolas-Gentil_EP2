# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 17:09:51 2015

@author: Nicolas Laloni Gentil

Projeto 2 - Jogo da Forca!

"""

# Projeto de Nicolas Gentil

from random import choice               # Importando a função random
    
from unicodedata import normalize               # Importando a função normalize

arquivo = open('entrada.txt', encoding="utf-8")               # Selecionando o arquivo com a lista

conteudo = arquivo.readlines()               # cria uma lista do arquivo


palavras = []              # Cria uma lista das palavras já usadas

chutes = 0              # Definindo os chutes    


def média_de_tentativas(chutes, palavras):
    return chutes/len(palavras)
        


# Limpando a lista de palavras

limpa = []               # Criando uma lista de palavras limpas

for palavra in conteudo:              # Faz com que o comando do strip repita em cada palavra
    p = palavra.strip()               
    if p != "":               # Elimina a linha em branco
        limpa.append(p)               # Adiciona as palavras limpas para a nova lista
    

restart = 0               # Definindo restart

while restart == 0:

    import turtle               # Importando a biblioteca de turtle graphics
    
    
    window = turtle.Screen()               # criando uma janela
    window.bgcolor("Yellow")
    window.title("Jogo da Forca")               # Criando um título para o jogo
    turtle.speed(0)               # Definindo a velocidade da tartaruga
    
    turtle2 = turtle.Turtle()               # criando uma nova tartaruga
    turtle2.speed(0)               # Definindo a velocidade da tartaruga
    turtle2.pensize(8)               # Definindo a grossura da caneta
    turtle2.hideturtle()               # Escondendo a tartaruga
    
    turtle3 = turtle.Turtle()               # criando uma nova tartaruga
    turtle3.pensize(4)               # Definindo a grossura da caneta
    turtle3.speed(0)               # Definindo a velocidade da tartaruga
    turtle3.hideturtle()               # Escondendo a tartaruga
    
    turtle4 = turtle.Turtle()               # criando uma nova tartaruga
    turtle4.pensize(8)               # Definindo a grossura da caneta
    turtle4.speed(0)               # Definindo a velocidade da tartaruga
    turtle4.hideturtle()               # Escondendo a tartaruga
    
    turtle5 = turtle.Turtle()               # criando uma nova tartaruga
    turtle5.pensize(8)               # Definindo a grossura da caneta
    turtle5.speed(0)               # Definindo a velocidade da tartaruga
    turtle5.hideturtle()               # Escondendo a tartaruga
    
    turtle6 = turtle.Turtle()               # criando uma nova tartaruga
    turtle6.pensize(8)               # Definindo a grossura da caneta
    turtle6.speed(0)               # Definindo a velocidade da tartaruga
    turtle6.hideturtle()               # Escondendo a tartaruga
    
    turtle7 = turtle.Turtle()               # criando uma nova tartaruga
    turtle7.pensize(8)               # Definindo a grossura da caneta
    turtle7.speed(0)               # Definindo a velocidade da tartaruga
    turtle7.hideturtle()               # Escondendo a tartaruga
    
    
    
    # Comandos da função normalize, que irá retirar os acentos e maiusculas das palavras 
    
    def formatar(txt):
        return normalize('NFKD', txt).encode('ASCII','ignore').decode('ASCII')
    if __name__ == '__main__':
        from doctest import testmod
        testmod()    
    
    
    # Criando um random para a lista
    
    esc = choice(limpa)              # Palavra que será randomizada

    
    limpa.remove(esc)               # Remove a palavra já escolhida
    
    palavras.append(esc)              # Adiciona a palavra escolhida na lista de palavras escolhidas
    
    
    # Criando a lista das palavras formatadas
    
    formatada = (formatar(esc)).lower()              # Palavra formatada minuscula
     
             
    # Criando a forca
             
    def forca():         
    
        turtle.hideturtle()
        turtle.pensize(8)
        
        turtle.penup()
        turtle.setx(-200)
        turtle.sety(-100)
        turtle.pendown()
        turtle.left(90)
        turtle.fd(300)
        turtle.right(90)
        turtle.fd(100)
        turtle.right(90)
        turtle.fd(100)
        turtle.left(90)
        
    forca()    
    
    # Criando a cabeça
    
    def cabeca():
    
        turtle2.penup()
        turtle2.setpos(-100, 100)
        turtle2.right(180)
        turtle2.pendown()
        turtle2.begin_fill()
        turtle2.fillcolor("Blue")
        turtle2.circle(30)
        turtle2.end_fill()
    
    # Criando o corpo
    
    def corpo():
    
        turtle2.penup()
        turtle2.left(90)
        turtle2.fd(60)
        turtle2.pendown()
        turtle2.fd(70)  
    
    # Criando a primeira perna
    
    def perna1():
    
        turtle2.right(30)
        turtle2.fd(50)
        turtle2.penup()
        turtle2.setx(-100)
        turtle2.sety(-30) 
    
    # Criando a segunda perna
    
    def perna2():
    
        turtle2.pendown()
        turtle2.left(60)
        turtle2.fd(50)

    # Criando o primeiro braço
    
    def braco1():
    
        turtle2.penup()
        turtle2.setx(-100)
        turtle2.sety(5)
        turtle2.left(60)
        turtle2.pendown()
        turtle2.fd(30)

    # Criando o segundo braço
    
    def braco2():
        
        turtle2.penup()
        turtle2.right(180)
        turtle2.pendown()
        turtle2.fd(60)

    # Criando os olhos
    
    def olhos():
        
        turtle2.penup()
        turtle2.setx(-100)
        turtle2.sety(100)
        turtle2.left(90)
        turtle2.fd(20)
        turtle2.right(90)
        turtle2.fd(10)
        turtle2.pendown()
        turtle2.circle(2)
        turtle2.penup()
        turtle2.left(180)
        turtle2.fd(20)
        turtle2.right(180)
        turtle2.pendown()
        turtle2.circle(2)
    
    # Criando a boca
    
    def boca():
        
        turtle2.penup()
        turtle2.setx(-100)
        turtle2.sety(100)
        turtle2.left(90)
        turtle2.fd(40)
        turtle2.pendown()
        turtle2.left(90)
        turtle2.fd(10)
        turtle2.right(180)
        turtle2.fd(20)

    # Criando a função espaço entre os traços
    
    def espaco():
        
        turtle3.penup()
        turtle3.fd(15)
        turtle3.pendown()
        
    # Definindo os traços
        
    def tracos():    
        
        turtle3.penup()
        turtle3.setx(-200)
        turtle3.sety(-200)
        turtle3.pendown()
            
            
        for c in esc:
            if c == ' ':
                espaco()
                
            else:    
                turtle3.fd(15)
                turtle3.penup()
                turtle3.fd(5)
                turtle3.pendown()
            
    
    tracos()
    
    
    # Definindo o letreiro errou
    
    def errou():
        
        turtle4.color('Red')        
        turtle4.penup()
        turtle4.setpos(50, 125)
        turtle4.pendown()
        turtle4.write('ERROU!', font = ('Arial', 30))
        
    # Definindo o letreiro acertou

    def acertou():
        
        turtle4.color('Green')
        turtle4.penup()
        turtle4.setpos(50, 125)
        turtle4.pendown()
        turtle4.write('ACERTOU!', font = ('Arial', 30))
        
    # Definindo o letreiro da média  
        
    def placar():
        turtle6.penup()
        turtle6.setpos(-50, 50)
        turtle6.pendown()
        turtle6.write('Média de chutes por palavra:', font = ('Arial', 20))
        
    placar()     
        
        
    # Definindo a turtle que escreve a média 
        
    def escreve_media():
        turtle5.penup()
        turtle5.setpos(70, 20)
        turtle5.pendown()
        turtle5.write(int(média_de_tentativas(chutes, palavras)), font = ('Arial', 20))
        
    escreve_media() 
    
    # Definindo o letreiro vc ganhou
    
    def vc_ganhou():
        turtle7.color('Green')
        turtle7.penup()
        turtle7.setpos(-50, 125)
        turtle7.pendown()
        turtle7.write('VOCÊ GANHOU!', font = ('Arial', 30))
        
    # Definindo o letreiro vc perdeu
        
    def vc_perdeu():
        turtle7.color('Red')
        turtle7.penup()
        turtle7.setpos(-50, 125)
        turtle7.pendown()
        turtle7.write('VOCÊ PERDEU!', font = ('Arial', 30))    
        
        
    ja_usadas = []              # Cria uma lista das letras já inseridas

    
    # Criando a função while para repetir o programa
    
    acertos = 0
    erros = 0
    
    for e in range(0,len(formatada)):              # Conta cada espaço da palavra escolhida 

        if formatada[e] == ' ':              # Aumenta o placar dos acertos a cada espaço
            acertos += 1
    
    while erros < 8 and restart==0:
        
        p = window.textinput("Pergunta", "Insira uma letra:")              # Input da letra escolhida
        p = p.lower()

        while p in ja_usadas or len(p)>1:
            p = window.textinput('Já usada ou mais de uma letra', 'Letra já foi utilizada ou você digitou mais de uma letra, insira outra letra:')
            p = p.lower()
            
        ja_usadas.append(p)              # Adiciona a letra escolhida na lista das já usadas    
            
        for i in range(0,len(formatada)):              # Escreve as letras
                
            if p == formatada[i]:
                
                turtle3.penup()
                turtle3.setx(-200+i*20)
                turtle3.sety(-185)
                turtle3.pendown()   
                turtle3.write((esc[i]).upper(), font = ("Arial",18))
                
                acertos += 1
                chutes += 1
                
                turtle4.clear()
                
                acertou()
                
        if p not in formatada:
                erros += 1
                chutes += 1
            
        if erros == 1 and p not in formatada:              # Desenha a cabeça
           cabeca()
           turtle4.clear()
           errou()
           
        if erros == 2 and p not in formatada:              # Desenha o corpo
            corpo()
            turtle4.clear()
            errou()
            
        if erros == 3 and p not in formatada:              # Desenha a perna
            perna1()
            turtle4.clear()
            errou()
            
        if erros == 4 and p not in formatada:              # Desenha a perna
            perna2()
            turtle4.clear()
            errou()
            
        if erros == 5 and p not in formatada:              # Desenha o braço
            braco1()
            turtle4.clear()
            errou()
            
        if erros == 6 and p not in formatada:              # Desenha o braço
            braco2()
            turtle4.clear()
            errou()
            
        if erros == 7 and p not in formatada:              # Desenha os olhos
            olhos()
            turtle4.clear()
            errou()
            
        if erros == 8 and p not in formatada:              # Desenha a boca
            boca()
            turtle4.clear()
            vc_perdeu()
            restart = 1
            
            
        if acertos == len(formatada):
            turtle4.clear()
            vc_ganhou()
            restart = 1
            
    f = window.textinput("Fim", "Fim do jogo! Se quiser jogar de novo, digite s, senão, n")
    if f == "s" or f == "S":
        turtle.clear()
        turtle2.clear()
        turtle3.clear()
        turtle4.clear()
        turtle5.clear()
        turtle6.clear()
        turtle7.clear()
        
        restart = 0
        
    else:
        break
           
            
        
        
        
        