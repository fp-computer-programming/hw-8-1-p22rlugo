# Ryan Lugo: RJL 12/9/21

def safe_card():
    card_one = input("What is your first cards points?: ")
    card_two = input("What is your second card points?: ")

    card_value = int(card_one) + int(card_two)
    safe = "Nil"

    if card_value < 21:
        safe = "You are safe!"
    else:
        safe = "You are not safe."
    return safe

print(safe_card())