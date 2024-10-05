import random
def roll_dice(numbers=3, points=None):
    print('<<<ROLL THE DICE>>>')
    if points is None:
        points = []
    while numbers > 0:
        points.append(random.randrange(1, 7))
        numbers = numbers - 1
    return points
def roll_result(total):
    isBig = 11 <= total <= 18
    isSmall = 3 <= total <= 10
    if isBig:
        return 'Big'
    elif isSmall:
        return 'Small'
def start_game():
    money = int(input('How much you want to start: ')) 
    print(f'You start with {money} dollars.')
    while money > 0:
        print('<<<<<<<<<  GAME STARTS!  >>>>>>>>>')
        choices = ['Big', 'Small']
        your_choice = input('Big or Small: ').capitalize()
        if your_choice not in choices:
            print('Invalid choice. Please select "Big" or "Small".')
            continue
        bet = int(input('How much you wanna bet? - '))
        if bet > money:
            print(f"You don't have enough money! You have {money} now.")
            continue
        points = roll_dice()
        total = sum(points)
        result = roll_result(total)
        print(f'<<<ROLL THE DICE! >>>')
        print(f'The points are {points}') 
        if your_choice == result:
            print(f'You Win! You gained {bet} dollars.')
            money += bet  # 贏錢，金額增加
        else:
            print(f'You Lose! You lost {bet} dollars.')
            money -= bet  # 輸錢，金額減少
        print(f'You now have {money} dollars.')
    print('GAME OVER! You have no money left.')

start_game()
