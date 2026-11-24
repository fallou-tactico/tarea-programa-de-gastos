def agregar_gasto(lista_gastos):
    descripcion = input("Descripción del gasto: ")

    
    while True:
        try:
            monto = float(input("Monto ($): "))
            if monto <= 0:
                print("Error: El monto debe ser mayor a 0.")
            else:
                break
        except ValueError:
            print("Error: Ingresa un número válido (ej. 12.50).")

    categoria = input("Categoría (Comida/Transporte/Ocio/Otros): ")

    
    nuevo_gasto = {
        "descripcion": descripcion,
        "monto": monto,
        "categoria": categoria
    }

    
    lista_gastos.append(nuevo_gasto)
    print("-> Gasto registrado con éxito.")



gastos = []
while True:
    print("\n=== GESTOR DE GASTOS ===")
    print("1. Registrar gasto")
    print("2. Ver todos los gastos")
    print("3. Filtrar por categoría")
    print("4. Ver resumen total")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        agregar_gasto(gastos)  
    elif opcion == "2":
        print("Elegiste ver gastos")
    elif opcion == "3":
        print("Elegiste Filtrar por categoría")
    elif opcion == "4":
        print("Ver resumen total")
    elif opcion == "5":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida")