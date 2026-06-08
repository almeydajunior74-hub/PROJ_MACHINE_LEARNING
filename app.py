#criando uma interface com streamli

import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression


dado=pd.read_csv("pizzas.csv")


modelo = LinearRegression()

x=dado[["diametro"]]
y=dado[["preco"]]

modelo.fit(x,y)




#criando interface com streamlit

st.title("🍕 Precificando corretamento o valor de uma Pizza 🍕")
st.divider()

diametro = st.number_input("digite o diâmetro da Pizza para saber o valor de venda: ")
if diametro:
    preco_previsto = modelo.predict([[diametro]])[0][0]
    st.write(f"<h1>o valor da pizza com diâmetro de {diametro:.2f}cm, é de R${preco_previsto:.2f}</h1>",unsafe_allow_html=True)
    st.balloons()
    

