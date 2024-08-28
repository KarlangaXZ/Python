import sys

user1 = input("Quien es el jugador 1?")
user2 = input("Quien es el jugador 2?")
user1_answer =  input("{}, Que vas elegir piedra, papel o tijeras?".format(user1))
user2_answer =  input("{}, Que vas elegir piedra, papel o tijeras?".format(user2))

def compare(u1, u2):
    if u1 == u2:
        return("Estan Empate!")
    elif u1 == 'piedra':
        if u2 == 'tijera':
            return("Gano Roca!")
        else:
            return("Gano Papel!")
    elif u1 == 'tijera':
        if u2 == 'papel':
            return("Gana Tijeras")
        else: 
            return("Gano Roca!")
    elif u1 == 'papel':
        if u2 == 'piedra':
            return ("Gana Papel!")
        else:
            return("Gano tijera")
    else:
        return("ALGO SALIO MAL!, No se inserto Piedra, Papel o Tijeras, Intenta nuevamente.")
        sys.exit()

print(compare(user1_answer.lower(), user2_answer.lower()))