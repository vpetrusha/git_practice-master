import random


def set_team_rating(side):
    while True:
        try:
            team_rating = int(input(f"Enter {side} team rating [1-10]: "))
            if team_rating > 10 or team_rating < 0:
                raise ValueError(f"Invalid input. Pick a number from 0 to 10: ")
        except ValueError as error:
            print(error)
            pass
        else:
            return team_rating


def set_team_form(side):
    while True:
        try:
            team_form = int(input(f"Enter {side} team form value [-3 to 3]: "))
            if team_form not in range(-3,4) :
                raise ValueError("Invalid form input. Pick a number from -3 to 3: ")
        except ValueError as error:
            print(error)
            pass
        else:
            return team_form


def dice_roll():
    home_team_rating = set_team_rating('home')
    away_team_rating = set_team_rating('away')

    home_team_form = set_team_form('home')
    away_team_form = set_team_form('away')

    ratio = 4

    dice_roll_home = home_team_rating + home_team_form + ratio
    dice_roll_away = away_team_rating + away_team_form + ratio

    dice_roll_home_list = [random.randint(1, 6) for x in range(dice_roll_home)]
    dice_roll_away_list = [random.randint(1, 6) for x in range(dice_roll_away)]

    print(f"Dice roll results:{dice_roll_home_list} and {dice_roll_away_list}")
    print(f"The probable score is {dice_roll_home_list.count(6)} : {dice_roll_away_list.count(6)}")


dice_roll()