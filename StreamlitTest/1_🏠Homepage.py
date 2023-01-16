import streamlit as st
st.set_page_config(
    page_title="HELLO",
    page_icon='😊'

)
st.title("Main Page")
st.sidebar.success("SELECT A PAGE ")

if 'my_input' not in st.session_state:
    st.session_state['my_input'] = ''
my_input = st.text_input("Input a text", st.session_state['my_input'])
submit = st.button("Submit")
if submit:
    st.session_state['my_input'] = my_input
    st.write("You have entered:", my_input)

    