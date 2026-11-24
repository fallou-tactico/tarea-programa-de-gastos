def agregar_gasto(gastos):
    descripcion = input("Descripción del gasto: ").strip()
    while not descripcion:
        print("Error: La descripción no puede estar vacía.")
        descripcion = input("Descripción del gasto: ").strip()

    while True:
        try:
            monto = float(input("Monto ($): "))
            if monto <= 0:
                print("Error: El monto debe ser mayor a 0.")
            else:
                break
        except ValueError:
            print("Error: Por favor, ingresa un número válido.")

    categoria = input("Categoría (Comida/Transporte/Ocio/Otros): ").strip()
    if not categoria:
        categoria = "Otros"
    else:
        categoria = categoria.capitalize()

    nuevo_gasto = {
        "descripcion": descripcion,
        "monto": monto,
        "categoria": categoria
    }
    
    gastos.append(nuevo_gasto)
    print("-> Gasto registrado con éxito.\n")


def mostrar_gastos(gastos):
    print("\n--- LISTA DE GASTOS ---")
    if not gastos:
        print("No hay gastos registrados aún.\n")
        return

    for indice, gasto in enumerate(gastos, start=1):
        print(f"{indice}. {gasto['descripcion']} | Categoría: {gasto['categoria']} | Monto: ${gasto['monto']:.2f}")
    print()


def filtrar_por_categoria(gastos):
    print("\n--- FILTRAR POR CATEGORÍA ---")
    if not gastos:
        print("No hay gastos registrados para filtrar.\n")
        return

    categoria_buscada = input("Ingresa la categoría a buscar: ").strip().capitalize()
    gastos_filtrados = [g for g in gastos if g["categoria"] == categoria_buscada]

    if not gastos_filtrados:
        print(f"No se encontraron gastos en la categoría '{categoria_buscada}'.\n")
    else:
        print(f"\nGastos en '{categoria_buscada}':")
        for indice, gasto in enumerate(gastos_filtrados, start=1):
            print(f"{indice}. {gasto['descripcion']} - ${gasto['monto']:.2f}")
        print()


def calcular_resumen(gastos):
    print("\nRESUMEN DE GASTOS")
    if not gastos:
        print("Total general: $0.00")
        print("No hay gastos registrados para desglosar.\n")
        return

    total_general = 0.0
    totales_por_categoria = {}

    for gasto in gastos:
        monto = gasto["monto"]
        categoria = gasto["categoria"]
        
        total_general += monto
        
        if categoria in totales_por_categoria:
            totales_por_categoria[categoria] += monto
        else:
            totales_por_categoria[categoria] = monto

    print(f"Total general: ${total_general:.2f}")
    for categoria, total in totales_por_categoria.items():
        print(f"* {categoria}: ${total:.2f}")
    print()


def main():
    lista_gastos = []

    while True:
        print("=== GESTOR DE GASTOS ===")
        print("1. Registrar gasto")
        print("2. Ver todos los gastos")
        print("3. Filtrar por categoría")
        print("4. Ver resumen total")
        print("5. Salir")

        try:
            opcion = int(input("Elige una opción: "))
        except ValueError:
            print("Error: Debes ingresar un número del 1 al 5.\n")
            continue

        if opcion == 1:
            agregar_gasto(lista_gastos)
        elif opcion == 2:
            mostrar_gastos(lista_gastos)
        elif opcion == 3:
            filtrar_por_categoria(lista_gastos)
        elif opcion == 4:
            calcular_resumen(lista_gastos)
        elif opcion == 5:
            print("¡Gracias por usar el Gestor de Gastos! Hasta luego.")
            break
        else:
            print("Opción no válida. Por favor, elige un número entre 1 y 5.\n")


if __name__ == "__main__":
    main()
