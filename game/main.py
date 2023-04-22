import random

def choose_option():
    user_option = input('selecciona piedra, papel o tijera: ')
    user_option = user_option.lower()
    options = ('piedra', 'papel', 'tijera')
    computer_option = random.choice(options)
    if user_option not in options:
        print('Ingresa una opción valida')
        return None,None
    return user_option, computer_option

def rules(user_option, computer_option, user_win, computer_win):
    if user_option == None:
        print('Vuelve a Intentarlo por favor')
    elif user_option == computer_option:
        print('Amigo han empatado')
    elif (user_option == 'piedra' and computer_option == 'tijera') or (user_option == 'papel' and computer_option == 'piedra') or (user_option == 'tijera' and computer_option == 'papel'):
        print(f'Felicidades has ganado, la computadora escogió {computer_option}')
        user_win += 1
    else:
        print(f'Has perdido, la computadora escogió {computer_option}')
        computer_win += 1
    return user_win, computer_win
# La función run es la encargada de controlar el flujo del juego "piedra, papel o tijera". Al principio, se inicializan tres variables: rounds, user_win y computer_win. La variable rounds lleva la cuenta de la cantidad de rondas que se han jugado, mientras que user_win y computer_win llevan la cuenta de las victorias del usuario y de la computadora, respectivamente.

# Luego, se inicia un ciclo while que se ejecutará mientras user_win sea menor a 2 y computer_win sea menor a 2. Esto significa que el juego continuará hasta que alguno de los dos participantes haya ganado dos rondas.

# Dentro del ciclo while, se imprime en pantalla una separación de líneas con el símbolo *, seguido del número de la ronda actual y nuevamente una separación de líneas con el símbolo *. Luego, se imprime en pantalla la cantidad de victorias del usuario y de la computadora.

# A continuación, se llama a la función choose_option para que el usuario elija su opción y se le asigna el resultado de esta función a las variables user_option y computer_option.

# Luego, se llama a la función rules pasando como argumentos las variables user_option, computer_option, user_win y computer_win. Esta función determina quién gana la ronda y actualiza las variables user_win y computer_win

def run():
    rounds = 1
    user_win = 0
    computer_win = 0
    while user_win < 2 and computer_win < 2:
        print('*' * 12)
        print(f'ROUND {rounds}')
        print('*' * 12)

        print(f'User >> {user_win}')
        print(f'Computer >> {computer_win}')

        user_option, computer_option = choose_option()

        user_win, computer_win = rules(user_option, computer_option, user_win, computer_win)

        if user_win == 2:
            print('El juego ha terminado')
        elif computer_win == 2:
            print('El juego ha terminado')
        else:
            rounds += 1  

if __name__ == '__main__':
    run()
