import streamlit as st

def main(): 
    st.title('Hello World')
    st.markdown('Botao')
    botao = st.button('Botao')
    if botao:
      st.markdown('Clicado')

    st.markdown('Ckeckbox')
    check = st.checkbox('Checkbox')
    if check:
      st.markdown('Clicado')

    st.markdown('Radio')
    radio = st.radio('Escolha as opções:',('Opt 1', 'Opt 2'))
    if radio == 'Opt 1':
        st.markdown('Opt 1')
    if radio == 'Opt 2':
        st.markdown('Opt 2')

    st.markdown('Selectbox')
    select = st.selectbox('Escolha as opções:',('Opt 1', 'Opt 2'))
    if select == 'Opt 1':
        st.markdown('Opt 1')
    if select == 'Opt 2':
        st.markdown('Opt 2')

    st.markdown('Multiselect')
    multi = st.multiselect('Escolha as opções:',('Opt 1', 'Opt 2', 'Opt 3'))
    if multi == 'Opt 1':
        st.markdown('Opt 1')
    if multi == 'Opt 2':
        st.markdown('Opt 2')
    if multi == 'Opt 3':
        st.markdown('Opt 3')

    st.markdown('File uploader')
    file = st.file_uploader('Escolha as opções:', type = 'csv')
    if file is not None:
        st.markdown('Não esta vazio!')
 


if __name__=='__main__':
  main()