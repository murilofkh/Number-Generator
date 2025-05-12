import random
import time

seu_nome = "Murilo"
print(f"This program is desenvolved to == {seu_nome} ==")
print("Press Enter to generate a random number or write 'exit'")

while True:
    user_input = input("Press Enter or write 'random'\n")
    if user_input == "" or user_input == "random":
        print(f"The choose number is: {random.choice(range(1, 100))}")
    elif user_input == "exit":
        print("wait a moment", end="")
        for _ in range(5):           
            time.sleep(1)
            print(".", end="", flush=True)
        print() 
        break
    if user_input == "exit now" :
        time.sleep(0.8)
        print("You exit now. The program is shutdown now")
        time.sleep(0.5)
        break
    if user_input == "list" :
        print("this command not exist. try other")
    else:
        print("This command not exist. try again")

    