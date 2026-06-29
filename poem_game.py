# Collaborative Poem Game - Console Based
# Parts 1-4: Player Setup + Random Selection + Game State + Game Loop

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


def create_game_state(players):
    """Initialise and return a fresh game state dictionary."""
    return {
        "players": players,
        "turn_order": [],
        "current_turn_index": 0,
        "poem_lines": [],        # list of (player_name, line) tuples
        "turns_completed": 0,
        "game_over": False,
    }


def current_player(state):
    """Return the name of the player whose turn it is."""
    return state["turn_order"][state["current_turn_index"]]


def add_line(state, player, line):
    """Record a poem line and advance the turn index."""
    state["poem_lines"].append((player, line))
    state["turns_completed"] += 1
    state["current_turn_index"] += 1


def is_game_over(state):
    """Return True when every player has had exactly one turn."""
    return state["turns_completed"] >= len(state["players"])


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


def prompt_player_for_line(state):
    """Ask the current player to enter their poem line and record it."""
    player = current_player(state)
    turn_num = state["turns_completed"] + 1
    total = len(state["players"])

    print(f"--- Turn {turn_num} of {total} ---")
    print(f"It's {player}'s turn.")
    line = input(f"{player}, enter your line: ").strip()
    add_line(state, player, line)
    print()


def run_game_loop(state):
    """Drive the game from first turn to last."""
    print("=" * 50)
    print("   LET THE POEM BEGIN!")
    print("=" * 50)
    print()

    while not is_game_over(state):
        prompt_player_for_line(state)


if __name__ == "__main__":
    players = get_players()
    state = create_game_state(players)
    starter = pick_starting_player(players)
    state["turn_order"] = get_turn_order(players, starter)
    run_game_loop(state)
    print("[DEBUG] Game loop finished.")
    print(f"[DEBUG] Lines collected: {state['poem_lines']}")
