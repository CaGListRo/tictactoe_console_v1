import os
import sys

def init_game(field_unit, won=False):
    if won:
        for i in range(0, 10):
            field_unit.clear()
    for i in range(0, 10):
        field_unit.append(i + 1)


def check_winning(field_unit):
    winning = False
    # check columns
    for i in range(0, 3):
        if field_unit[i] == field_unit[i + 3] and field_unit[i + 3] == field_unit[i + 6]:
            winning = True
    line = True
    line_number = 0
    while line:
        if field_unit[line_number] == field_unit[line_number + 1] and field_unit[line_number + 1] == field_unit[line_number + 2]:
            winning = True
            break
        line_number += 3
        if line_number > 7:
            line = False
    if field_unit[0] == field_unit[4] and field_unit[4] == field_unit[8]:
        winning = True
    if field_unit[2] == field_unit[4] and field_unit[4] == field_unit[6]:
        winning = True
    return winning

def player_swab(player):
    if player == 1:
        player = 2
    else:
        player = 1
    return player

def get_input(player, field_unit):
    while True:
        field = input(f"Spieler {player} ist am Zug. Zahl des Feldes eingeben: ")
        if field.isdigit():
            field = int(field)
            if 0 < field < 10:
                if field_unit[field - 1] == field:
                    break
                elif field_unit[field - 1] != field:
                    sys.stdout.write(f"Feld schon belegt, versuche es erneut Spieler {player}\n")
            else:
                sys.stdout.write("Nur Zahlen zwischen 1 und 9 sind erlaubt.\n")
        else:
            sys.stdout.write("Bitte eine Zahl eingeben...\n") 
    return field          

def print_field(field_unit):
    os.system("cls")
    column_counter = 0
    line_counter = 0
    for i in range(0, 9):
        column_counter += 1 
        if column_counter == 3:
            column_counter = 0
            sys.stdout.write(" | " + str(field_unit[i]) + " |\n")
            line_counter += 1
            if line_counter < 3:
                sys.stdout.write("---------------\n")
            else:
                sys.stdout.write("\n")
        else:
            sys.stdout.write(" | " + str(field_unit[i]))

def main():
    field_unit = []
    init_game(field_unit)
    run = True
    player = 1
    turn_counter = 0
    while run:
        print_field(field_unit)
        field = get_input(player, field_unit)
        
        if player == 1:
            field_unit[field - 1] = "X"
            won = check_winning(field_unit)
            if not won:
                player = player_swab(player)
        elif player == 2:
            field_unit[field - 1] = "O"
            won = check_winning(field_unit)
            if not won:
                player = 1
        turn_counter += 1
        if won or turn_counter >= 9:
            print_field(field_unit)
            if won:
                print(f"Spieler {player} hat gewonnen!")
            else:
                print("Unentschieden!")
            again = input("Nochmal? (j/n) ")
            if again.lower() == "j":
                init_game(field_unit, won)
                won = False
                player = player_swab(player)
            else:
                print("Tschüss...")

main()