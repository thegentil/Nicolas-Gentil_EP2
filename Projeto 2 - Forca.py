# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 17:09:51 2015

@author: Nicolas Laloni Gentil

Projeto 2 - Jogo da Forca!

"""

# Projeto de Nicolas Gentil

import turtle               # Importando a biblioteca de turtle graphics
window = turtle.Screen()               # criando uma janela
window.bgcolor("lightblue")               # Definindo a cor de fundo para azul
window.title("Jogo da Forca")               # Criando um título para o jogo

from random import choice               # Importando a função random

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

esc = choice(limpa)

print(len(esc))
  
         
# Definindo a posição da forca
         
def forca():         

    turtle.hideturtle()
    
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
    
forca()    

# Criando a cabeça

def cabeca():

    turtle.penup()
    turtle.right(90)
    turtle.pendown()
    turtle.circle(30)
    turtle.fillcolor("yellow")    # Algum erro, perguntar

cabeca()

# Criando o corpo

def corpo():

    turtle.penup()
    turtle.left(90)
    turtle.fd(60)
    turtle.pendown()
    turtle.fd(70)
    
corpo()    

# Criando a primeira perna

def perna1():

    turtle.right(30)
    turtle.fd(50)
    turtle.penup()
    turtle.setx(-100)
    turtle.sety(-30) 

perna1()

# Criando a segunda perna

def perna2():

    turtle.pendown()
    turtle.left(60)
    turtle.fd(50)

perna2()    

# Criando o primeiro braço

def braco1():

    turtle.penup()
    turtle.setx(-100)
    turtle.sety(5)
    turtle.left(60)
    turtle.pendown()
    turtle.fd(30)
    
braco1()    

# Criando o segundo braço

def braco2():
    
    turtle.penup()
    turtle.right(180)
    turtle.pendown()
    turtle.fd(60)
    
braco2()    

# Criando os olhos

def olhos():
    
    turtle.penup()
    turtle.setx(-100)
    turtle.sety(100)
    turtle.left(90)
    turtle.fd(20)
    turtle.right(90)
    turtle.fd(10)
    turtle.pendown()
    turtle.circle(2)
    turtle.penup()
    turtle.left(180)
    turtle.fd(20)
    turtle.right(180)
    turtle.pendown()
    turtle.circle(2)
    
olhos()    

# Criando a boca

def boca():
    
    turtle.penup()
    turtle.setx(-100)
    turtle.sety(100)
    turtle.left(90)
    turtle.fd(40)
    turtle.pendown()
    turtle.left(90)
    turtle.fd(10)
    turtle.right(180)
    turtle.fd(20)
    
boca()    

# Definindo os espaços que estarão as letras

if len(esc) == 7:
    
    turtle.penup()
    turtle.setx(-200)
    turtle.sety(-200)
    turtle.pendown()
    turtle.right(180)
    
    turtle.fd(20)
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()
    
    turtle.fd(20)
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()
    
    turtle.fd(20)
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()
    
    turtle.fd(20)
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()
    
    turtle.fd(20)
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()
    
    turtle.fd(20)
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()
    
    turtle.fd(20)
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()
    
    
if len(esc) == 9:
    
    turtle.penup()
    turtle.setx(-200)
    turtle.sety(-200)
    turtle.pendown()
    turtle.right(180)
    
    turtle.fd(20)
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()
    
    turtle.fd(20)
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()
    
    turtle.fd(20)
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()
    
    turtle.fd(20)
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()
    
    turtle.fd(20)
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()
    
    turtle.fd(20)
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()
    
    turtle.fd(20)
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()
    
    turtle.fd(20)
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()
    
    turtle.fd(20)
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()
    

if len(esc) == 10:
    
    turtle.penup()
    turtle.setx(-200)
    turtle.sety(-200)
    turtle.pendown()
    turtle.right(180)
    
    turtle.fd(20)
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()
    
    turtle.fd(20)
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()
    
    turtle.fd(20)
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()
    
    turtle.fd(20)
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()
    
    turtle.fd(20)
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()
    
    turtle.fd(20)
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()
    
    turtle.fd(20)
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()
    
    turtle.fd(20)
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()
    
    turtle.fd(20)
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()
    
    turtle.fd(20)
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()
    

if len(esc) == 12:
    
    turtle.penup()
    turtle.setx(-200)
    turtle.sety(-200)
    turtle.pendown()
    turtle.right(180)
    
    turtle.fd(20)
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()
    
    turtle.fd(20)
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()
    
    turtle.fd(20)
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()
    
    turtle.fd(20)
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()
    
    turtle.fd(20)
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()
    
    turtle.fd(20)
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()
    
    turtle.fd(20)
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()
    
    turtle.fd(20)
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()
    
    turtle.fd(20)
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()
    
    turtle.fd(20)
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()
    
    turtle.fd(20)
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()
    
    turtle.fd(20)
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()
     

if len(esc) == 21:
    
    turtle.penup()
    turtle.setx(-200)
    turtle.sety(-200)
    turtle.pendown()
    turtle.right(180)
    
    turtle.fd(20)
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()
    
    turtle.fd(20)
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()
    
    turtle.fd(20)
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()
    
    turtle.penup()
    turtle.fd(30)
    turtle.pendown()
    
    turtle.fd(20)
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()
    
    turtle.fd(20)
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()
    
    turtle.fd(20)
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()
    
    turtle.fd(20)
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()
    
    turtle.fd(20)
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()
    
    turtle.fd(20)
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()
    
    turtle.fd(20)
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()
    
    turtle.fd(20)
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()
    
    turtle.penup()
    turtle.fd(30)
    turtle.pendown()
    
    turtle.fd(20)
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()
    
    turtle.fd(20)
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()
    
    turtle.penup()
    turtle.fd(30)
    turtle.pendown()
    
    turtle.fd(20)
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()
    
    turtle.fd(20)
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()
    
    turtle.fd(20)
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()
    
    turtle.fd(20)
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()
    
    turtle.fd(20)
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()
    
      

# Criando a função while para repetir o programa

x = 0

while x == 0:
    
    #if 
    

    
    p = window.textinput("Pergunta", "Insira uma letra:")
    
    if p in limpa(0):
        
        turtle
    
    
    
    