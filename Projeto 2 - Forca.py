# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 17:09:51 2015

@author: Nicolas Laloni Gentil

Projeto 2 - Jogo da Forca!

"""

# Projeto de Nicolas Gentil

restart = 0

while restart == 0:

    import turtle               # Importando a biblioteca de turtle graphics
    
    
    window = turtle.Screen()               # criando uma janela
    window.bgcolor("lightblue")               # Definindo a cor de fundo para azul
    window.title("Jogo da Forca")               # Criando um título para o jogo
    turtle.speed(0)
    turtle.screensize(2000,800)
    
    turtle2 = turtle.Turtle()
    turtle2.speed(0)
    turtle2.pensize(8)
    turtle2.hideturtle()
    
    turtle3 = turtle.Turtle()
    turtle3.pensize(8)
    turtle3.speed(0)
    turtle3.hideturtle()
    
    from random import choice               # Importando a função random
    
    from unicodedata import normalize               # Importando a função normalize
    
    # Comandos da função normalize, que irá retirar os acentos e maiusculas das palavras 
    
    def formatar(txt):
        return normalize('NFKD', txt).encode('ASCII','ignore').decode('ASCII')
    if __name__ == '__main__':
        from doctest import testmod
        testmod()    
    
    # Selecionando o arquivo com a lista
    
    arquivo = open('entrada.txt', encoding="utf-8")
    
    conteudo = arquivo.readlines()               # cria uma lista do arquivo
    
    
    # Limpando a lista de palavras
    
    limpa = []
    
    for palavra in conteudo:              # Faz com que o comando do strip repita em cada palavra
        p = palavra.strip()               
        if p != "":               # Elimina a linha em branco
            limpa.append(p)               # Adiciona as palavras limpas para a nova lista
    
    
    # Criando um random para a lista
    
    esc = choice(limpa)              # Palavra que será randomizada
    
    print(len(esc))
    
    print(limpa)
    
    print(esc)
    
    # Criando a lista das palavras formatadas
    
    formatada = (formatar(esc)).lower()              # Palavra formatada
    
    print(formatada)
    
    
      
             
    # Definindo a posição da forca
             
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
        turtle2.fillcolor("yellow")
        turtle2.circle(30)
         
    
    #cabeca()
    
    # Criando o corpo
    
    def corpo():
    
        turtle2.penup()
        turtle2.left(90)
        turtle2.fd(60)
        turtle2.pendown()
        turtle2.fd(70)
        
    #corpo()    
    
    # Criando a primeira perna
    
    def perna1():
    
        turtle2.right(30)
        turtle2.fd(50)
        turtle2.penup()
        turtle2.setx(-100)
        turtle2.sety(-30) 
    
    #perna1()
    
    # Criando a segunda perna
    
    def perna2():
    
        turtle2.pendown()
        turtle2.left(60)
        turtle2.fd(50)
    
    #perna2()    
    
    # Criando o primeiro braço
    
    def braco1():
    
        turtle2.penup()
        turtle2.setx(-100)
        turtle2.sety(5)
        turtle2.left(60)
        turtle2.pendown()
        turtle2.fd(30)
        
    #braco1()    
    
    # Criando o segundo braço
    
    def braco2():
        
        turtle2.penup()
        turtle2.right(180)
        turtle2.pendown()
        turtle2.fd(60)
        
    #braco2()    
    
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
        
    #olhos()    
    
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
        
    #boca()    
    
    # Criando a função espaço entre os traços
    
    def espaco():
        
        turtle3.penup()
        turtle3.fd(30)
        turtle3.pendown()
        
    # Definindo os traços
        
    def tracos():    
        
        turtle3.penup()
        turtle3.setx(-300)
        turtle3.sety(-200)
        turtle3.pendown()
            
            
        for c in esc:
            turtle3.fd(20)
            turtle3.penup()
            turtle3.fd(10)
            turtle3.pendown()
            
            if c == ' ':
                espaco()    
    
    tracos()
    
    
    # Criando a função while para repetir o programa
    
    acertos = 0
    erros = 0
    
    while erros <= 8:
        
        p = window.textinput("Pergunta", "Insira uma letra:")
            
        for i in range(0,len(formatada)):

            if formatada[i] == ' ':
                acertos += 1
                
            if p == formatada[i]:
                
                turtle3.penup()
                turtle3.setx(-300+i*30)
                turtle3.sety(-185)
                turtle3.pendown()   
                turtle3.write(p, font= ("Arial",25))
                
                acertos += 1
                print(acertos)
                
        if p not in formatada:
                erros += 1
            
        if erros == 1 and p not in formatada:
           cabeca()
           
        if erros == 2 and p not in formatada:
            corpo()
            
        if erros == 3 and p not in formatada:
            perna1()
            
        if erros == 4 and p not in formatada:
            perna2()
            
        if erros == 5 and p not in formatada:
            braco1()
            
        if erros == 6 and p not in formatada:
            braco2()
            
        if erros == 7 and p not in formatada:
            olhos()
            
        if erros == 8 and p not in formatada:
            boca()
            restart = 1
            
        if acertos >= len(formatada)-1:
            restart = 1
            
    f = window.textinput("Fim", "Fim do jogo! Se quiser jogar de novo, digite s, senão, n")
    if f == "s" or f == "S":
        turtle.clear()
        turtle2.clear()
        turtle3.clear()
        restart = 0
        
    else:
        break
           
            
        
        
        
        