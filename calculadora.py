# calculadora.py
# Aplicación de Calculadora interactiva John Otero

print("=====================================")
print("      CALCULADORA INTERACTIVA")
print("=====================================")


historial = []

def pedir_numero(texto):
    while True:
        try:
            return float(input(texto))
        except ValueError:
            print("⚠️  Error: introduce un número válido.")

def mostrar_menu():
    
    print("\nSelecciona la operación que deseas realizar:")
    print("  1. Suma (+)")
    print("  2. Resta (-)")
    print("  3. Multiplicación (*)")
    print("  4. División (/)")
    print("  5. Potencia (^)")
    print("  6. Raíz cuadrada (√)")
    print("  7. Ver historial")
    print("  8. Salir")

def realizar_operacion():
    
    operacion = input("Operación (+, -, *, /, ^, √): ")

    if operacion in ['+', '-', '*', '/', '^']:
        numero_1 = pedir_numero("Primer número: ")
        numero_2 = pedir_numero("Segundo número: ")
    elif operacion == '√':
        numero_1 = pedir_numero("Número: ")
        numero_2 = None
    else:
        print("❌ Operación no reconocida.")
        return

    if operacion == '+':
        resultado = numero_1 + numero_2
        print("Resultado:", resultado)
        historial.append(f"{numero_1} + {numero_2} = {resultado}")

    elif operacion == '-':
        resultado = numero_1 - numero_2
        print("Resultado:", resultado)
        historial.append(f"{numero_1} - {numero_2} = {resultado}")

    elif operacion == '*':
        resultado = numero_1 * numero_2
        print("Resultado:", resultado)
        historial.append(f"{numero_1} * {numero_2} = {resultado}")

    elif operacion == '/':
        if numero_2 != 0:
            resultado = numero_1 / numero_2
            print("Resultado:", resultado)
            historial.append(f"{numero_1} / {numero_2} = {resultado}")
        else:
            print("❌ Error: no se puede dividir por cero.")

    elif operacion == '^':
        resultado = numero_1 ** numero_2
        print("Resultado:", resultado)
        historial.append(f"{numero_1} ^ {numero_2} = {resultado}")

    elif operacion == '√':
        if numero_1 >= 0:
            resultado = numero_1 ** 0.5
            print("Resultado:", resultado)
            historial.append(f"√{numero_1} = {resultado}")
        else:
            print("❌ Error: no se puede calcular la raíz de un número negativo.")

def mostrar_historial():
    
    if len(historial) == 0:
        print("No hay operaciones registradas todavía.")
    else:
        print("\n📜 HISTORIAL DE OPERACIONES:")
        for i, op in enumerate(historial, start=1):
            print(f"{i}. {op}")


while True:
    mostrar_menu()
    opcion = input("Elige una opción (1-8): ")

    if opcion in ['1', '2', '3', '4', '5', '6']:
        realizar_operacion()
    elif opcion == '7':
        mostrar_historial()
    elif opcion == '8':
        print("\n👋 Gracias por usar la calculadora. ¡Hasta pronto!")
        break
    else:
        print("⚠️  Opción no válida. Intenta de nuevo.")

    continuar = input("\n¿Deseas realizar otra operación? (s/n): ").lower()
    if continuar != 's':
        print("\n👋 Programa finalizado. ¡Hasta luego!")
        break