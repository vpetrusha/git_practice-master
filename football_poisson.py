from random import randint

def random_with_N_digits():
    range_start = 1
    range_end = 6
    return randint(range_start, range_end)
    
print(random_with_N_digits())

username = input("Enter username:")
print("Username is: " username)
