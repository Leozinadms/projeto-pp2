import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.title("Bem-vindo ao Meu Site com teste de leozika")
st.write("Este é um exemplo de um site criado por leozika.")

st.sidebar.title("Navegação")
st.sidebar.title("automatização")
page = st.sidebar.selectbox("Escolha uma página:", ["Home", "Sobre", "Contato"])
page = st.sidebar.selectbox("entar no wpp:", ["numero de wpp","65996411634"])
page = st.sidebar.selectbox("escolhe qual opção:",["start","incio","numero"])
if page == "Home":
    st.header("Home")
    st.write("Bem-vindo à página inicial!")

    data = pd.DataFrame({
        'Categoria': ['A', 'B', 'C'],
        'Valores': [10, 20, 30]
    })
    st.write(data)

    fig, ax = plt.subplots()
    ax.bar(data['Categoria'], data['Valores'])
    st.pyplot(fig)

elif page == "Sobre":
    st.header("Sobre")
    st.header("vamos entrar?")
    st.write("Este site foi criado como um exemplo de uso do Streamlit.")

elif page == "Contato":
    st.header("Contato")
    st.write("Você pode entrar em contato conosco pelo email: exemplo@dominio.com")
elif page == "adicionar contato":
    st.header("meu numero 65996411634")
    st.write("entrar em conato")
#Upload de Arquivos
st.sidebar.header("Upload de Arquivos")
st.sidebar.header("sua musica")
uploaded_file = st.sidebar.file_uploader("Escolha um arquivo")
uploaded_file = st.sidebar.file_uploader("musica que voce gosta")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write(data)

# Widgets Interativos
if st.button("Clique aqui"):
    st.write("Botão clicado!")

age = st.slider("Selecione sua idade", 0, 100, 25)
st.write("Sua idade é:", age)
