import streamlit as st

def main():
    # Funciones para las operaciones
    def sumar(a, b):
        return a + b
    
    def restar(a, b):
        return a - b
    
    def multiplicar(a, b):
        return a * b

    def dividir(a, b):
        return a / b if b != 0 else "No se puede dividir por cero"

    # Título de la app
    st.title("🧮 Calculadora Básica")

    # Entrada de números
    num1 = st.number_input("Ingrese el primer número", value=0.0, step=0.1)
    num2 = st.number_input("Ingrese el segundo número", value=0.0, step=0.1)

    # Selección de operación
    operacion = st.selectbox("Seleccione una operación", ["Suma", "Resta", "Multiplicar", "Dividir"])

    # Cálculo usando funciones
    resultado = None
    if operacion == "Suma":
        resultado = sumar(num1, num2)

    elif operacion == "Resta":
        resultado = restar(num1, num2)

    elif operacion == "Multiplicar":
        resultado = multiplicar(num1, num2)

    elif operacion == "Dividir":
        resultado = dividir(num1, num2)
    
    # Mostrar resultado
    if resultado is not None:
        st.success(f"El resultado de la {operacion.lower()} es: {resultado}")

if __name__ == "__main__":
    main()




