import streamlit

streamlit.title('My Mom\'s Healthy Diner')
streamlit.header('Breakfast Favourites')
streamlit.text('🥣Omega 3 & Blue Berry Oatmeal')
streamlit.text('🍨Kale, Spinach & Rocket - Smoothie')
streamlit.text('🥚Hard Boiled Free - Range Egg')
streamlit.text('🥑🍞Avocado Toast')
streamlit.header('🍌🥭Build Your Own Fruit Smoothie 🥑🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

my_fruit_list = my_fruit_list.set_index('Fruit')
# Lets put a pick list here to eneable picking fruit desired
streamlit.multiselect("Pick some fruit :",list(my_fruit_list.index))
# Display the table on the page
streamlit.dataframe(my_fruit_list)
