import os, time, random
make_piles = lambda: [1, 3, 5, 7]
display_piles = lambda piles: os.system('clear') or [print(f"Pile {i+1}: " + "|"*pile) for i, pile in enumerate(piles)] or print("\n")
is_game_over = lambda piles: all(pile == 0 for pile in piles)
calculate_nim_sum = lambda piles: sum([nim_sum := nim_sum ^ pile for pile in piles] or [nim_sum := 0])
random_move = lambda piles: (chosen := random.choice([i for i, pile in enumerate(piles) if pile > 0]), random.randint(1, piles[chosen]))
best_move = lambda piles: next(((i, piles[i] - (target := piles[i] ^ (nim_sum := calculate_nim_sum(piles)))) for i in range(len(piles)) if target < piles[i]), next((i, 1) for i in range(len(piles)) if piles[i] > 0))
ai_move = lambda piles, ai_difficulty: best_move(piles) if random.randint(ai_difficulty, 5) == 5 else random_move(piles)
def game_loop(gamemode, p1, p2, ai_diff=5):
    piles, player = make_piles(), 1
    while not is_game_over(piles):
        display_piles(piles); current_player = p1 if player == 1 else p2
        if gamemode == None: print(f"{current_player}'s turn!\n")
        valid = False
        while not valid:
            if gamemode == None or (gamemode == "ai" and player == 1):
                if gamemode == "ai": print(f"{p1}'s Turn!\n")
                try:
                    pile = int(input(f"Choose a pile 1-{len(piles)}: ")) - 1; print("\n")
                    if pile < 0 or pile >= len(piles) or piles[pile] <= 0: print("Invalid pile.\n"); time.sleep(1); break
                    remove = int(input(f"How many to remove from pile {pile + 1}? "))
                    if remove < 1 or remove > piles[pile]: print(f"\nInvalid. Can remove 1 to {piles[pile]}.\n"); time.sleep(1); break
                    else: piles[pile] -= remove; valid = True; player = 2 if player == 1 else 1
                except (ValueError, IndexError): print("\nInvalid input.\n")
            elif gamemode == "ai" and player == 2:
                print("AI's turn!\n"); pile, remove = ai_move(piles, ai_diff); time.sleep(1)
                if pile is not None: piles[pile] -= remove; print(f"AI removed {remove} from pile {pile + 1}.\n"); player = 2 if player == 1 else 1; valid = True
                time.sleep(2)
    display_piles(piles)
    if gamemode == "ai" and player == 2: print(f"{p1}, you lost to the AI!\n")
    elif gamemode == "ai" and player == 1: print(f"Congrats, {p1}, you beat the AI!\n")
    else: print(f"{p2 if player == 2 else p1} won!\n")
    print("Returning...\n"); time.sleep(3); os.system('clear')
def main():
    print("Welcome to Nim!\n"); time.sleep(1)
    p1 = input("Enter Player 1's name: ").strip()
    while True:
        choice = input(f"\nPlay (l)ocally or against (ai), {p1}? ").lower()
        if choice in ['l', 'local']: p2 = input("\nEnter Player 2's name: ").strip(); game_loop(None, p1, p2)
        elif choice == 'ai':
            p2 = "AI"
            while True: 
                diff = int(input("\nSelect AI difficulty [1 - 5(hard)]: "))
                if 1 <= diff <= 5: game_loop("ai", p1, p2, diff); break
                else: print("Invalid.\n")
        else: print("Invalid choice!\n"); time.sleep(1)
os.system('clear'); main()
