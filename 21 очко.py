import random

def draw_card():
    return random.randint(2, 11)

def calculate_sum(hand):
    return sum(hand)

def display_hands(player, dealer, hide_dealer_second_card=True):
    print(f"\nТвои карты: {player} | Сумма: {calculate_sum(player)}")
    if hide_dealer_second_card:
        print(f"Карта дилера: [{dealer[0]}, ?]")
    else:
        print(f"Карты дилера: {dealer} | Сумма: {calculate_sum(dealer)}")

def player_turn(player_hand):
    while True:
        total = calculate_sum(player_hand)
        if total == 21:
            print("Ты набрал 21 очко! Победа!")
            return 'win'  # Возвращаем флаг победы
        choice = input("Взять карту? (да/нет): ").strip().lower()
        if choice in ('да', 'д', 'y', 'yes'):
            card = draw_card()
            player_hand.append(card)
            print(f"Ты взял карту: {card} | Сумма теперь: {calculate_sum(player_hand)}")
            total = calculate_sum(player_hand)
            if total == 21:
                print("Ты набрал 21 очко! Победа!")
                return 'win'
            elif total > 21:
                print("Перебор! Ты проиграл.")
                return 'lose'
        elif choice in ('нет', 'н', 'no', 'n'):
            return 'continue'
        else:
            print("Пиши 'да' или 'нет'.")

def dealer_turn(dealer_hand):
    print("\nХод дилера...")
    while calculate_sum(dealer_hand) < 17:
        card = draw_card()
        dealer_hand.append(card)
        print(f"Дилер берёт карту: {card}")
    print(f"Карты дилера: {dealer_hand} | Сумма: {calculate_sum(dealer_hand)}")
    return calculate_sum(dealer_hand)

def determine_winner(player_sum, dealer_sum):
    if dealer_sum > 21:
        print("У дилера перебор! Ты выиграл.")
    elif dealer_sum == 21:
        print("У дилера 21 очко! Ты проиграл.")
    elif player_sum > dealer_sum:
        print("Ты выиграл!")
    elif player_sum < dealer_sum:
        print("Ты проиграл.")
    else:
        print("Ничья.")

def play_game():
    print("=== Добро пожаловать в игру '21 очко' ===")
    player = [draw_card(), draw_card()]
    dealer = [draw_card(), draw_card()]

    display_hands(player, dealer)

    if calculate_sum(player) == 21:
        print("Ты сразу набрал 21 очко! Победа!")
        return

    result = player_turn(player)

    if result == 'win':
        return
    elif result == 'lose':
        return

    display_hands(player, dealer, hide_dealer_second_card=False)

    if calculate_sum(dealer) == 21:
        print("У дилера сразу 21 очко! Ты проиграл.")
        return

    dealer_sum = dealer_turn(dealer)
    determine_winner(calculate_sum(player), dealer_sum)

if __name__ == "__main__":
    play_game()
