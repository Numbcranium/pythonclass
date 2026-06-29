# Collaborative Poem Game - Console Based
# Parts 1-2: Player Setup + Random Selection

import random

def get_players():
    """Collect player names from input."""
    print("=" * 50)
    print("   COLLABORATIVE POEM GAME")
    print("=" * 50)
    print()

    while True:
        try:
            count = int(input("How many players will be playing? "))
            if count < 2:
                print("You need at least 2 players.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    players = []
    print()
    for i in range(count):
        while True:
            name = input(f"Enter name for Player {i + 1}: ").strip()
            if not name:
                print("Name cannot be empty.")
            elif name in players:
                print("That name is already taken.")
            else:
                players.append(name)
                break

    print()
    print(f"Players registered: {', '.join(players)}")
    print()
    return players


def pick_starting_player(players):
    """Randomly select the first player to start the poem."""
    starter = random.choice(players)
    print(f"Randomly selecting who goes first...")
    print(f">>> {starter} will start the poem! <<<")
    print()
    return starter


def get_turn_order(players, starter):
    """Build a randomised turn order starting from the selected player."""
    remaining = [p for p in players if p != starter]
    random.shuffle(remaining)
    order = [starter] + remaining
    print("Turn order for this round:")
    for i, name in enumerate(order, 1):
        print(f"  {i}. {name}")
    print()
    return order


if __name__ == "__main__":
    players = get_players()
    starter = pick_starting_player(players)
    turn_order = get_turn_order(players, starter)
    print(f"[DEBUG] Turn order: {turn_order}")
