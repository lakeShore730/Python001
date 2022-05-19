import random

def is_player_win(player, computer):
    if (player == "r" and computer == "s") or ( player == "s" and computer == "p") and (player == "p" and computer == "r"):
        return True
    return False


def play():
    user = input("R for rock, P for paper or S for scissor : ").lower()
    
    if not user in ["r", "p", "s"]:
        return "Invalid input"
       
    computer = random.choice(["r", 'p', 's'])

    print(f"Yours : {user}")
    print(f"Computer: {computer}")
        
    if user == computer:
        return "Tie"

    if is_player_win(user, computer):
        return "You won"
    return "You lost"
    

while True:
    result = play()
    print(result)