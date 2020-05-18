import streamlit as st

def main(): 
  st.title('Hello World')
  st.header('This is a header')
  st.subheader('This is a subheader')
  st.text('This is a text')
  st.image('logo.png')
  st.subheader('This is a audio')
  st.audio('record.wav') 
  st.subheader('This is a video')
  st.video('sentiment_motion.mov')

if __name__=='__main__':
  main()