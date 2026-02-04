import streamlit as st

def tabuada(n1):
    exibicao = ""
    for i in range (1, 11):
        exibicao = exibicao + f"{n1} X {i} = {n1 * i}\n"
    return exibicao
       


st.title("Gerador de tabuadas")

n1 = st.number_input("Qual o valor da tabuada a ser gerada?", step = 1)

if st.button("Exibir tabuada"):
    st.subheader(f"Tabuada do {n1}")
    st.text(tabuada(n1))


