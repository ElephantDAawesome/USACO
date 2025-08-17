


#1
# for i in range(6):
#     for j in range(i):
#         print('*', end=' ')
#     print()


#2
# for i in range(7):
#     for j in range(1, i):
#         print(j, end=' ')
#     print()

#3
# for i in range(5, 0, -1):
#     for j in range(i):
#         print('*', end=' ')
#     print()

#4
# b = 0
# for i in range(6, 0, -1):
#     b += 1
#     for j in range(i):

#         print(b, end=' ')
#     print()


#5
# for i in range(6):
#     for j in range(i):
#         print('*', end='')
#     print()















# list1 = [1,2,3]
# list2 = [4,5,6]

# for i in list1:
#     for j in list2:
#         print(i,j)
#     print()


# for i in range(5):
#     for j in range(3):
#         print(j, end=' ')
#     print()




    # 0 1

# for i in range(4):
#     for j in range(5):
#         print(i, j, end=' ')
#     print()



# for i in range(6):
#     for j in range(i):
#         print(i , end=' ')
#     print()


# counter = 0
# flag = True
# while flag:
#     counter += 1
#     if counter > 6:
#         flag = False

#     counter2 = 0
#     flag2 = True
#     while flag2:
#         counter2 += 1
#         if counter2 > 6:
#             flag2 = False
#         print(counter)

# x = 0
# while (x<6):
#     y = 0
#     while(y < x):
#         print(x, end=' ')
#         y+=1
#     x += 1
#     print()
# for i in range(0, 101):
#     print(i*7)

# x = 0
# while (x<101):
#     print(x*7)
#     x +=7

# import random

# def guessing_game():
#     num = random.randint(0,11)
#     bool = True
#     while bool:
#         guess = int(input("Guess random number from 1 to 10: "))
#         if guess > num:
#             print("Number is to high, guess lower")
#         elif guess == num:
#             bool = False
#             print(f"Good job, the answer was: {num}")
#         else:
#             print("Number too low, guess again")

# guessing_game()

# list = ["A", "B", "C"]
# temp = list[0]

# list[0] = list[2]
# list[2] = list[1]
# list[1] = temp
# print(list)
# list[0] = list[2]
# list[1] = list[0]
# list[2] = list[1]
# print(list)

# list_abc = ["A", "B", "C"]



# def listswap(i, j, list_name):
#     #swap i and j 
#     temp = list_name[i]
#     list_name[i] = list_name[j]
#     list_name[j] = temp
#     return list_name

# print(listswap(0, 1, list_abc))

list_swaps = [[1,2,3], [3,2,1], [1,3,1]]

list_shells = ['A', 'B', 'C']
score = 0


def switch_var(index1, index2, list):
    return 0
for x in list_swaps:
    switchvar(x[0], x[1], list_shells)
