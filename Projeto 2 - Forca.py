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

# Selecionando o arquivo com a lista

L = open('Lista de palavras - Jogo da forca.txt', encoding="utf-8")

l = L.readlines()

print(l)

# Criando a função while para repetir o programa

x = 0

while x == 0:
    
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
    
    p = window.textinput("Pergunta", "Insira uma letra:")
    
    
    
    