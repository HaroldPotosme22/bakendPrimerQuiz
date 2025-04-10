def mostrar_menu():
    print("\n--- MENÚ INTERACTIVO ---")
    print("1. Mostrar un mensaje")
    print("2. Mostrar una lista de nombres")
    print("3. Salir del programa")
# Lista predefinida de nombres
nombres = ["Ana", "Luis", "Carlos", "María", "Sofía"]
# Bucle principal del programa
while True:
    mostrar_menu()
    opcion = input("Elige una opción (1, 2, 3): ").strip()

    if opcion == "1":
        print("\n🌟 ¡Sigue adelante! Estás haciendo un gran trabajo. 🌟")
    elif opcion == "2":
        print("\nLista de nombres:")
        for nombre in nombres:
            print(f"- {nombre}")
    elif opcion == "3":
        print("Gracias por usar el programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, elige 1, 2 o 3.")
