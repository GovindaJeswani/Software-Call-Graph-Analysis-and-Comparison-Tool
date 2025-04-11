def save_high_score(player_name, time_taken):
    with open("high_scores.txt", "a") as file:
        file.write(f"{player_name},{time_taken}\n")

def load_high_scores():
    try:
        with open("high_scores.txt", "r") as file:
            scores = [line.strip().split(",") for line in file.readlines()]
            return sorted(scores, key=lambda x: int(x[1]))
    except FileNotFoundError:
        return []
