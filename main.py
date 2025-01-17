import streamlit as st
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
st.write("Top suggestions, starting with the most suggested:")
st.write(top_10)
st.write("Input a ticker (i.e. AAPL, in that format) to search the database. If the ticker is in the database, the suggestion will be shown below.")
search = st.text_input("Input ticker here")
if search != "":
    with st.spinner("Searching for ticker: "+search):
        success = False
        for item in loaded_data.splitlines():
            if search.upper().strip() in item:
                st.write(item)
                success = True
                break
        if not success:
            st.write("Ticker not found in database.")