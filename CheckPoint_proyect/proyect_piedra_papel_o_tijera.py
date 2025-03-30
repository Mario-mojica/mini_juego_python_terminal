import random

def intro():
    print("\n=== Bienvenido a Aventura Terminal ===")
    print("\n* Eres un valiente explorador que ha sido transportado a una galaxia desconocida.")
    print(" Tu misión es sobrevivir, tomar decisiones sabias y encontrar la salida.\n")
    start_adventure()

def start_adventure():
    print("Te encuentras en la nave espacial principal. Hay dos puertas frente a ti:")
    print("1. Una puerta que lleva a la sala de control.")
    print("2. Una puerta que lleva al hangar de escape.")
    choice = input("\nElige tu destino (1 o 2): ")

    if choice == "1":
        control_room()
    elif choice == "2":
        hangar_escape()
    else:
        print("\nPor favor, selecciona una opción válida.")
        start_adventure()

def control_room():
    print("\nHas entrado a la sala de control. Las luces parpadean y hay un panel de control con dos opciones:")
    print("1. Activar el sistema de defensa de la nave.")
    print("2. Escanear los alrededores en busca de señales de vida.")
    choice = input("\n¿Qué haces? (1 o 2): ")

    if choice == "1":
        print("\nActivaste el sistema de defensa, pero accidentalmente disparaste a tu nave. Game Over.")
        retry()
    elif choice == "2":
        print("\nDetectaste una señal de vida en un planeta cercano. Decides investigar más de cerca.")
        planet_exploration()
    else:
        print("\nPor favor, selecciona una opción válida.")
        control_room()

def hangar_escape():
    print("\nEl hangar está lleno de cápsulas de escape. Algunas parecen dañadas:")
    print("1. Subir a la cápsula más cercana, aunque está algo rota.")
    print("2. Buscar otra cápsula en mejor estado.")
    choice = input("\n¿Qué haces? (1 o 2): ")

    if choice == "1":
        print("\nLa cápsula explota al despegar. Game Over.")
        retry()
    elif choice == "2":
        print("\nEncontraste una cápsula en buen estado y te diriges al planeta cercano.")
        planet_exploration()
    else:
        print("\nPor favor, selecciona una opción válida.")
        hangar_escape()

def planet_exploration():
    print("\nHas llegado al planeta. El ambiente parece hostil, pero también hay recursos valiosos.")
    print("1. Explorar el área en busca de comida y agua.")
    print("2. Construir un refugio para protegerte.")
    choice = input("\n¿Qué haces? (1 o 2): ")

    if choice == "1":
        print("\nEncuentras comida, pero un alienígena te ataca. Debes defenderte.")
        alien_battle()
    elif choice == "2":
        print("\nConstruyes un refugio, pero al no buscar comida, te debilitas. Game Over.")
        retry()
    else:
        print("\nPor favor, selecciona una opción válida.")
        planet_exploration()

def alien_battle():
    player_hp = 50
    alien_hp = 40

    print("\n=== Batalla contra el alienígena ===")
    while player_hp > 0 and alien_hp > 0:
        print(f"\nTu HP: {player_hp}")
        print(f"HP del alienígena: {alien_hp}")
        print("\n1. Atacar")
        print("2. Bloquear")
        print("3. Sanarte")
        action = input("\n¿Qué haces? (1, 2 o 3): ")

        if action == "1":
            damage = random.randint(10, 20)
            alien_hp -= damage
            print(f"\nLe hiciste {damage} de daño al alienígena.")
        elif action == "2":
            print("\nBloqueaste el ataque del alienígena.")
            continue
        elif action == "3":
            heal = random.randint(10, 15)
            player_hp += heal
            print(f"\nTe sanaste {heal} puntos de vida.")
        else:
            print("\nPor favor, selecciona una opción válida.")
            continue

        if alien_hp > 0:
            alien_damage = random.randint(5, 15)
            player_hp -= alien_damage
            print(f"El alienígena te hizo {alien_damage} de daño.")

    if player_hp > 0:
        print("\nHas derrotado al alienígena y encuentras un mapa que te lleva a casa. ¡Ganaste!")
    else:
        print("\nEl alienígena te derrotó. Game Over.")
        retry()

def retry():
    choice = input("\n¿Quieres intentarlo de nuevo? (s/n): ")
    if choice.lower() == "s":
        intro()
    else:
        print("\nGracias por jugar. ¡Hasta la próxima!")

if __name__ == "__main__":
    intro()
