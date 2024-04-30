import random

victorias = 0
derrotas = 0
empates = 0

def jugar():
    global victorias, derrotas, empates

    while True:
        usuario = input("Escoge una opcion: Piedra, Papel o Tijera:\n").lower()

        if usuario not in ['piedra', 'papel', 'tijera', 'Piedra', 'Papel', 'Tijera', 'PIEDRA', 'PAPEL', 'TIJERA']:
            print("Opción no válida. Por favor, escoge Piedra, Papel o Tijera.")
            continue
        

        computadora = random.choice(['piedra', 'papel', 'tijera'])

        if usuario == computadora:
            empates += 1
            print (f'Mi eleccion fue la misma! Empate!')
        else:
            if gano_el_jugador(usuario, computadora):
                victorias += 1
                print (f'Mi eleccion es {computadora}. Ganaste!')
            else:
                derrotas += 1
                print (f'Mi eleccion es {computadora}. Perdiste!')
        
        seguir_jugando = input("¿Quieres seguir jugando? (S/N): ").lower()
        print (f"Victorias: {victorias}, Derrotas: {derrotas}, Empates: {empates}")
        if seguir_jugando == 'n' or seguir_jugando == 'N':
            break
        elif seguir_jugando == 's' or seguir_jugando == 'S':
            continue
        else:
            print("No ingresaste S o N. Supongo que queres seguir jugando.")


def gano_el_jugador(jugador, oponente):
    #Retornar el valor true si gana el jugador.
    #como puede ganar el jugador? si el jugador selecciona piedra gana a tijera (r>s)
    #tijera le gana a papel (s>p)
    #papel le gana a piedra (p>r)
    #si alguno de estos valores es verdadero debemos retornar valor true, si no retornar false, si cualquiera es verdadero que retorne verdadero permite hacerlo el operardor or
    if ((jugador == 'piedra' and oponente == 'tijera')
        or (jugador == 'tijera' and oponente == 'papel')
        or (jugador == 'papel' and oponente == 'piedra')):
        return True
    #porque gano el jugador
    else:
        return False
    

print (jugar())


print(f"Victorias: {victorias}, Derrotas: {derrotas}, Empates: {empates}")