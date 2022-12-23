import streamlit as st

str_input = st.text_input('Take Input: ')
def convert_list(str_input):
    str_input=str_input.split()
    # st.write(str_list)
    return(str_input)
# convert_list(str_input)
if st.button("Return List "):
   st.write(convert_list(str_input))
# if st.button:
#     st.write(str_input)

def convert_upper(str_input):
    name_upper=[]
    str_input =str_input.split()
    for i in str_input:
        name_upper.append(i.upper())
    return(name_upper)
convert_upper(str_input)

if st.button("List in Upper Case"):
   st.write(convert_upper(str_input))

def count():
    counting = 0
    counter = convert_list(str_input)
    for i in counter:
        counting += 1
    return(counting)
if st.button('Print Count'):
   st.write(count())



