import streamlit as st
from streamlit_tags import st_tags
from backend import recipe_llm

def main():
    maxtags = st.slider('Number of ingredients available?', 1, 10, 3, key='jfnkerrnfvikwqejn')

    keywords = st_tags(
        label='# Enter Ingredients:',
        text='Press enter to add more',
        value=[],
        suggestions=['five', 'six', 'seven', 'eight', 'nine', 'three', 'eleven', 'ten', 'four'],
        maxtags=maxtags,
        key="aljnf")

    generate = st.button('Generate')
    st.write("### Recipe:")

    if generate:
        with st.spinner('Creating recipe.....'):
            st.write(recipe_llm(keywords))

if __name__ == '__main__':
    main()
