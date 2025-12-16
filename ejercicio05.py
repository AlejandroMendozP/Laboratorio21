class OperadorInvalidoError(Exception):
    pass

texto = input("Ingrese una cadena de texto: ")

try:

    separacion = texto.split()
    if len(separacion) != 3:
        raise ValueError("Valores invalidos")

    num1, operador, num2 = separacion
    num1_numero = float(num1)
    num2_numero = float(num2)

    if (operador != "+" and operador != "-" and operador != "*" and operador != "/"):
        raise OperadorInvalidoError("Operador no valido")

    match (operador):
        case "+":
            print(f"Suma: {num1_numero + num2_numero}")
        case "-":
            print(f"Resta: {num1_numero - num2_numero}")
        case "*":
            print(f"Multiplicacion: {num1_numero * num2_numero}")
        case "/":
            if (num1_numero == 0):
                raise ZeroDivisionError("No se puede dividir entre 0")
            print(f"Division: {num1_numero / num2_numero}")

except ValueError as e:
    print(f"Error: {e}")
except ZeroDivisionError as e:
    print(f"Error: {e}")
except OperadorInvalidoError as e:
    print(f"Error: {e}")
