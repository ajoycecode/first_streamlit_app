import streamlit
import pandas


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.title('My parents new healthy diner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Tocket Smoothie')
streamlit.text('🥑🍞 Hard-Boiled Free-Range Egg')


streamlit.header('🍌🍓 Build Your own Fruit Smootie 🥝🍇')


# Let's put apick list here so they can pick the fruit they want to include
streamlit.multiselect ("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])


streamlit.dataframe(my_fruit_list)
