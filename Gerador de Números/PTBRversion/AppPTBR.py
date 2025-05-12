import random
import time

seu_nome = "Murilo"
print(f"Este programa foi desenvolvido por == {seu_nome} ==")
print("Pressione Enter para gerar um número aleatório ou digite 'sair' ou 'exit' para sair")

while True:
    user_input = input("Aperte Enter ou digite random\n")
    if user_input == "" or user_input == "random":
        print(f"O número escolhido é: {random.choice(range(1, 100))}")
    elif user_input == "sair" or user_input == "exit":
        print("Aguarde um momento", end="")
        for _ in range(5):           
            time.sleep(1)
            print(".", end="", flush=True)
        print()  # Para pular uma linha após o movimento
        break
    if  user_input == "list" or user_input == "listar":
        print("O comando listar ou list não foi feito ou evoluído tente sair ou random")
    if user_input == "sair agora" or user_input == "exit now" :
        time.sleep(0.8)
        print("Você saiu a força, o programa será desligado")
        time.sleep(2.5)
        break    
    else:
        print("Comando inválido. Tente novamente.")

