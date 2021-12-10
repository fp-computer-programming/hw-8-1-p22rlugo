# Ryan Lugo: RJL 12/9/21

def safe_card(card1,card2):

    card_value = int(card1) + int(card2)
    safe = "Nil"

    if card_value < 21:
        safe = "You are safe!"
    else:
        safe = "You are not safe."
    return safe

card_one = input("What is your first cards points?: ")
card_two = input("What is your second card points?: ")

print(safe_card(card_one,card_two))