def binary_to_decimal(binary_str):
    return int(binary_str, 2)

def decimal_to_binary(decimal_num):
    return format(decimal_num, '08b')

def main():
    choice = input("Elija una opción: \n1. Convertir BINARIO a DECIMAL\n2. Convertir DECIMAL a BINARIO\n")
    
    if choice == '1':
        binary_str = input("Ingrese un número binario de 8 dígitos: ")
        if len(binary_str) == 8 and all(bit in '01' for bit in binary_str):
            print(f"El número decimal es: {binary_to_decimal(binary_str)}")
        else:
            print("Error: Debe ingresar un número binario de 8 dígitos.")
    
    elif choice == '2':
        decimal_num = int(input("Ingrese un número decimal (0-255): "))
        if 0 <= decimal_num <= 255:
            print(f"El número binario es: {decimal_to_binary(decimal_num)}")
        else:
            print("Error: Debe ingresar un número entre 0 y 255.")
    else:
        print("Opción no válida.")

main()