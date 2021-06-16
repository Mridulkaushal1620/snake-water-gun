import random


def convert(n):
    if n == "s" or n == "S":
        return 1
    elif n == "w" or n == "W":
        return 2
    elif n == "G" or n == "g":
        return 3
    else:
        return -1


def winner(n, m):
    if n > m:
        print("You won congrats!!")
    elif n < m:
        print("Comp won better luck next time")
    else:
        print("Draw")


# snake =1
# water = 2
# gun = 3
# i= user
# j = comp


j = random.randint(1, 4)
print("Welcome to the snake water gun game")
user_point = 0
comp_point = 0
print("How many raps you want to play")
k = 0
l = int(input())
while k < l:
    print("Enter 's' for snake, 'w' for and 'g' for gun")
    n = input()
    i = convert(n)
    if i == 1 and j == 2:
        print("your choice: snake")
        print("cpu choice: water")
        user_point += 1
        print("you: ", user_point)
        print("Comp: ", comp_point)
    elif i == 2 and j == 1:
        print("your choice: water")
        print("cpu choice: snake")
        comp_point += 1
        print("you: ", user_point)
        print("Comp: ", comp_point)
    elif i == 3 and j == 2:
        print("your choice: gun")
        print("cpu choice: water")
        comp_point += 1
        print("you: ", user_point)
        print("Comp: ", comp_point)
    elif i == 2 and j == 3:
        print("your choice: water")
        print("cpu choice: gun")
        user_point += 1
        print("you: ", user_point)
        print("Comp: ", comp_point)
    elif i == 1 and j == 3:
        print("your choice: snake")
        print("cpu choice: gun")
        comp_point += 1
        print("you: ", user_point)
        print("Comp: ", comp_point)
    elif i == 3 and j == 1:
        print("your choice: gun")
        print("cpu choice: snake")
        user_point += 1
        print("you: ", user_point)
        print("Comp: ", comp_point)
    elif i == j:
        print("clash")
        print("you: ", user_point)
        print("Comp: ", comp_point)
    else:
        print("you have entered wrong character")
    k += 1
winner(user_point, comp_point)