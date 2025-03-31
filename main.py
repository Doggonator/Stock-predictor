import streamlit as st
from difflib import SequenceMatcher

def similar(a, b):#for finding what ticker is the closest in a search
    #use my own alg, find similar characters and similar lengths
    similar_chars = 0
    lower_length = len(a)
    larger_length = len(b)
    if len(b) <lower_length:#in case the strings aren't the same length
        lower_length = len(b)
        larger_length = len(a)
    for i in range(0, lower_length):
        if a[i] == b[i]:
            similar_chars += 1
    similar_char_ratio = similar_chars/larger_length
    lengthdiff = abs(len(a)-len(b))
    lengthdiff_ratio = lengthdiff/larger_length
    return (similar_char_ratio+lengthdiff_ratio)/2

st.set_page_config(page_title="Stock suggestions", page_icon=None, layout="centered", initial_sidebar_state="auto", menu_items=None)
st.title("Stock suggestions")
st.caption("Created by Drew Warner")
#get the top choices
loaded_data = open("output.txt", "r").read()
top_10_lines = loaded_data.splitlines()[:10]
top_10 = ""
for item in top_10_lines:
    top_10 += item
    top_10 += ", \n"
st.write("Top suggestions, starting with the most suggested (Date is m-d-y):")
st.write(top_10)
st.write("Input a ticker (i.e. AAPL, in that format) to search the database. If the ticker is in the database, the suggestion will be shown below. If not, a stock with a close ticker will be shown")
search = st.text_input("Input ticker here")
if search != "":
    with st.spinner("Searching for ticker: "+search):
        data = loaded_data.splitlines()
        data.pop(0)#remove updated date
        best_score = similar(data[0], search.upper().strip())
        best = data[0]
        for item in data:
            this_score = similar(item, search.upper().strip())
            if this_score > best_score:
                best = item
                best_score = this_score
        st.write(best)