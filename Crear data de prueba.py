# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 05:29:18 2020

@author: PedroW10
"""

#Proyecto  grupal python 
#GRAFICOS ESTADISTICOS CON MATPLOTLIB
#TEMA: VIDEOJUEGOS
from faker import Faker
from faker_credit_score import CreditScore #usar para crear socre de juegos Fuente: https://pypi.org/project/faker-credit-score/
import pandas as pd
import random
fake = Faker()
fake.add_provider(CreditScore) #Instancia un objeto de Clase CreditScore #instalar en ananconda promtp :  pip install faker-credit-score



################################333333
#numero de filas de la base a crear
numero_casos=100000


fecha = []
usuario = []
puntaje = []
juego = []
tipo_juego = []
tiempo_juego = []
posicion_jugador = []
nivel = []
juegos =[{"nombre":"OSU", "tipo":"Arcade"},{"nombre":"Snake","tipo":"Estrategia"},{"nombre":"Mario", "tipo":"Aventura"},{"nombre":"GuitarHero", "tipo":"Acción"}]
for _ in range(numero_casos):
    #crea fechas de prueba
    fecha.append(fake.date(pattern='%Y-%m-%d', end_datetime=None))
    #crea usuarios de prueba
    usuario.append(fake.name())
    #crea puntaje de prueba
    puntaje.append(fake.credit_score())#instalar en ananconda promtp :  pip install faker-credit-score
    #crea nombre de juego # reemplazar los nombres despues    
    juego_random=random.choice(juegos)    
    juego.append(juego_random["nombre"])
        #crea usuarios de prueba
    tipo_juego.append(juego_random["tipo"])
    #crea usuarios de prueba
    tiempo_juego.append(random.random()*2)
    #crea usuarios de prueba
    posicion_jugador.append(random.choice(["Primero","Segundo","Tercero","Cuarto", "Quinto","Sexto","Séptimo","Octavo","Noveno","Décimo"]))
    #crea usuarios de prueba
    nivel.append(random.choice(["Facil","Intermedio","Dificil"]))


frame = { 'fecha': pd.Series(fecha), 'usuario': pd.Series(usuario), 'puntaje':pd.Series(puntaje), 'juego':pd.Series(juego), 'tipo_juego':pd.Series(tipo_juego), 'tiempo_juego':pd.Series(tiempo_juego), 'posicion_jugador':pd.Series(posicion_jugador), 'nivel':pd.Series(nivel)} 
df = pd.DataFrame(frame) #USAR ESTE DATAFRAME PARA LOS GRAFICOS

#pd.to_pickle(df,"C:\\Users\\PedroW10\\Documents\\GitHub\\graficos_python\\test.pickle")

