""" Calories again? """
def calories_count():
    """You are fat !!!"""
    total_calories = 0
    fruit_dict = {1 : 100, 2 : 120, 3 : 200, 4 : 60}

    while True :
        button = int(input())

        if button == 5:
            break

        total_calories += fruit_dict[button]

    print("Bye Bye")
    print(f"Total Calories: {total_calories}")
calories_count()
