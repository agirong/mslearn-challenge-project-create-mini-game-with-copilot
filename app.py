#crea un mini juego de consola, de pieda papel o tijera, donde el usuario juega contra la computadora, las entradas del usuario son rock,paper o scissors, y la computadora elige aleatoriamente una de las tres opciones, el juego termina cuando el usuario decide salir, y se muestra el puntaje final del usuario. Se debe validar que el usuario ingrese una de las tres opciones validas, si no es asi, se le debe indicar que la opcion no es valida y pedirle que ingrese una opcion valida.
#crealo en un archivo llamado app.py
# para ejecutarlo usa el comando python app.py
import random

def game():
   print("Bienvenido al juego de piedra, papel o tijera")
   user_score = 0; computer_score = 0; rondas = 0     
   while True:
       user_input = input("Ingrese rock, paper, scissors o salir: ")
       #pasar a minusculas
       user_input = user_input.lower()
       if user_input == "salir":
           print(f"Se jugaron {rondas} Partidas.Tu puntaje final es: {user_score} y el de la computadora es: {computer_score}")
           break
       elif user_input not in ["rock", "paper", "scissors"]:
           print("Opción no válida, intente de nuevo...")
           continue
       computer_input = random.choice(["rock", "paper", "scissors"])
       print(f"Tu eliges: {user_input}")
       print(f"Computadora elige: {computer_input}")
       rondas += 1
       if user_input == computer_input:
           print("Es un empate")
       elif user_input == "rock" and computer_input == "scissors":
           print("Ganaste")
           user_score += 1
       elif user_input == "paper" and computer_input == "rock":
           print("Ganaste")
           user_score += 1
       elif user_input == "scissors" and computer_input == "paper":
           print("Ganaste")
           user_score += 1
       else:
           computer_score += 1
           print("Perdiste")
game()





