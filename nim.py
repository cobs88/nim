import os
import time

def make_piles():
    piles = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]
    return piles

def display_piles(piles):
    os.system('clear')
    for i, pile in enumerate(piles):
        print(f"Pile {i + 1 if i + 1 >= 10 else ' ' + str(i + 1)}:", end=" ")
        print("|"*pile)
    print("\n")

def is_game_over(piles):
    return all(pile == 0 for pile in piles)

def calculate_nim_sum(piles):
    nim_sum = 0
    for pile in piles:
        nim_sum ^= pile
    return nim_sum


def ai_move(piles):
    nim_sum = calculate_nim_sum(piles)

    non_empty_piles = [pile for pile in piles if pile > 0]
    if len(non_empty_piles) == 2 and 1 in non_empty_piles:
        index_one = piles.index(1)
        index_other = piles.index(non_empty_piles[0] if non_empty_piles[1] == 1 else non_empty_piles[1])
        
        amount_to_remove = piles[index_other]

        return index_other, amount_to_remove

    if len(non_empty_piles) == 1:
        index_one = piles.index(non_empty_piles[0])

        amount_to_remove = non_empty_piles[0] - 1

        return index_one, amount_to_remove



    for i in range(len(piles)):
        target = piles[i] ^ nim_sum
        if target < piles[i]:
            amount_to_remove = piles[i] - target
            return i, amount_to_remove

    for i in range(len(piles)):
        if piles[i] > 0:
            return i, 1

def game_loop(gamemode):
    player = 1

    piles = make_piles()

    while not is_game_over(piles):
        display_piles(piles)
        nim_sum = calculate_nim_sum(piles)

        if gamemode == None: print(f"Player {player}'s turn!\n")
        valid_move = False
        
        while not valid_move:
            if gamemode == None or gamemode == "ai" and player == 1:
                if gamemode == "ai": print("Player's Turn!\n")
                try:
                    chosen_pile = int(input(f"Choose a pile number 1 to {len(piles)}: ")) - 1
                    print("\n")
                    if chosen_pile < 0 or chosen_pile > int(len(piles)) or piles[chosen_pile] <= 0:
                        print("Invalid pile number. Try again.\n")
                        time.sleep(1)
                        break

                    num_to_remove = int(input(f"How many objects to remove from pile {chosen_pile + 1}? "))

                    if num_to_remove < 1 or num_to_remove > piles[chosen_pile]:
                        print(f"\nInvalid number. You can remove 1 to {piles[chosen_pile]} objects.\n")
                        time.sleep(1)
                        break

                    else:
                        piles[chosen_pile] -= num_to_remove
                        valid_move = True

                        player = 2 if player == 1 else 1

                except (ValueError, IndexError):
                    print("\nInvalid input. Please enter numbers only.\n")

            elif gamemode == "ai" and player == 2:
                print("AI's turn!\n")
                chosen_pile, num_to_remove = ai_move(piles)
                time.sleep(1)
                if chosen_pile is not None:
                    piles[chosen_pile] -= num_to_remove
                    print(f"AI removed {num_to_remove} objects from pile {chosen_pile + 1}.\n")
                    player = 2 if player == 1 else 1
                    valid_move = True
                time.sleep(2)
    display_piles(piles)
    
    if gamemode == "ai" and player == 2: print("You lost to the ai!\n")
    elif gamemode == "ai" and player == 1: print("Congratulations, you beat the ai!\n")
    else: print(f"Player {player} won!\n")
    print("Returning to menu...\n")
    time.sleep(4)
    os.system('clear')

def main():
    print("Welcome to nim!\n")
    time.sleep(1)

    selected_mode = None
    while selected_mode == None:
        choice = input("Would you like to play (l)ocally or against (ai)? ")

        if choice in ['l', 'local', 'locally']:
            game_loop(None)
        elif choice in ['a', 'ai']:
            game_loop("ai")
        else:
            print("\nThats not a valid choice!\n")
            time.sleep(1)
os.system('clear')
main()