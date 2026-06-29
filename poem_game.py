# Collaborative Poem Game - Console Based
# Part 1: Player Setup

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


if __name__ == "__main__":
    players = get_players()
    print(f"[DEBUG] Players list: {players}")
