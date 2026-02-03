import streamlit as st

# Funções de cálculo
def calcular(v1, v2, operacao):
    if operacao == "Somar":
        return v1 + v2
    elif operacao == "Subtrair":
        return v1 - v2
    elif operacao == "Multiplicar":
        return v1 * v2
    elif operacao == "Dividir":
        return v1 / v2 if v2 != 0 else "Erro: Divisão por zero"

st.title("Calculadora Simples")
st.subheader("Feito com streamlit ❤️")

valor1 = st.number_input("Digite o primeiro valor:", value=0.0)
valor2 = st.number_input("Digite o segundo valor:", value=0.0)

operacao = st.selectbox("Escolha a operação:", ["Somar", "Subtrair", "Multiplicar", "Dividir"])

if st.button("Calcular"):
    resultado = calcular(valor1, valor2, operacao)
    
    st.markdown("---")
    st.text("Resultado:")
    if isinstance(resultado, str):
        st.error(resultado)
    else:
        st.success(f"O resultado é: {resultado}")