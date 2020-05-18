import streamlit as st
import pandas as pd

def main(): 
    st.title('Aceleradev Data Science')
    st.image('logo.png')
    file = st.file_uploader('Upload your file', type = 'csv')
    if file is not None:
        slider = st.slider('Valores', 1,100)
        df = pd.read_csv('IRIS.csv')

# Cria formato slider (deslizante)
        st.markdown('Slider')
        st.dataframe(df.head(slider))

# Cria formato tabela
        st.markdown('Table')
        st.table(df.head(slider))

#Mostrando as médias por espécies
        st.markdown('Média por espécie')
        st.table(df.groupby('species')['petal_width'].mean())



if __name__=='__main__':
  main()