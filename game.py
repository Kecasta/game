import random


options = ('piedra','papel','tijera')
win_jugador = 0
win_pc = 0
ronda = 1

while True:
   
    print ('\t ronda', ronda)
    print('\t JUGADOR', win_jugador,
          '\n\t COMPUTADOR', win_pc)
    

    player = input('\t<<<Elige tu opcion>>>\n\t piedra\n\t papel\n\t tijera \n\t =>').lower()
    pc_option= random.choice(options)

    print('\t computador',pc_option,'\n\t jugador', player)



    if player == 'piedra' and pc_option == 'piedra':
        print('ES UN EMPATE, JUEGUEN DE NUEVO')

    elif player == 'piedra' and pc_option == 'tijera':
        print('EL GANADOR ES EL JUGADOR, PIEDRA ROMPE TIJERA')
        win_jugador+=1
    elif player == 'piedra' and pc_option == 'papel':
        print('EL GANADOR ES EL COMPUTADOR, PAPEL ENVUELVE PIEDRA')
        win_pc+=1
    elif player == 'papel' and pc_option == 'piedra':
        print('EL GANADOR ES EL JUGADOR, PAPEL ENVUELVE PIEDRA')
        win_jugador+=1
    elif player == 'papel' and pc_option == 'papel':
        print('ES UN EMPATE, JUEGUEN DE NUEVO')
    elif player == 'papel' and pc_option == 'tijera':
        print('EL GANADOR ES EL COMPUTADOR, TIJERA CORTA PAPEL')
        win_pc+=1
    elif player == 'tijera' and pc_option == 'piedra':
        print('EL GANADOR ES EL COMPUTADOR, PIEDRA ROMPE TIJERA')
        win_pc+=1
    elif player == 'tijera' and pc_option == 'papel':
        print('EL GANADOR ES EL JUGADOR, TIJERA CORTA PAPLE')
        win_jugador+=1
    elif player == 'tijera' and pc_option == 'tijera':
        print('ES UN EMPATE, JUEGUEN DE NUEVO')

    if win_jugador == 2:
        print('\t<<<<EL CAMPEON ES EL JUGADOR>>>>')
        break
    elif win_pc == 2:
        print('\t<<<<EL CAMPEON ES EL COMPUTADOR>>>>')
        break
    ronda+=1