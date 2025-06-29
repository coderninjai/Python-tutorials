# Snake water Game
import random as r
user_choice=input("Enter your choice from Snake ,Water, Gun : ")

selector=["Snake","Water","Gun"]

result_matrix=[
    ["Draw","win","lose"],
    ["lose","Draw","win"],
    ["win","lose","Draw"]
]

computer_choice=r.choice(selector)
print(computer_choice)

if user_choice not in selector:
    print("Invalid Input  ")
    
else:
    user_index=selector.index(user_choice)
    computer_index=selector.index(computer_choice)
    
    result=result_matrix[user_index][computer_index]
    print("Player ",result, "This Round")