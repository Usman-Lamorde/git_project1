
import streamlit as st
from PIL import Image
import pandas as pd

img = Image.open("fruits vegetables.jpg")
st.image(img, width=700)
st.header("Fruits and Vegetables Calorie Counter")
st.subheader("This Application will calculate the total amount of calories in your food order.")

st.selectbox('Pick Gender', ['M', 'F'])
 
Selected = st.multiselect('Select ', ['Fresh Apple', 'Fresh Cantaloupe', 'Fresh Grapes', 'Cinnamon Apples', 'Fresh Pear', 'Fresh Banana', 'Diced Strawberries', 'Dried Cranberries', 'Diced Peaches', 'Applesauce', 'Diced Pears', 'Mixed Fruit', 'Raisins', 'Mandarin Oranges', 'Wild Blueberries', 'Baby Carrots', 'Celery Sticks', 'Broccoli Florets', 'Cucumber Slices', 'Grape Tomatoes', 'Garden Salad', 'Jicama Sticks', 'Steamed Broccoli', 'Red Peppers Strips', 'Black Charro Beans', 'Green Beans', 'Green Peas', 'Mashed Potatoes', 'Sweet Golden Corn', 'Sweet Potato Fries', 'Baked Beans'])
             
Fruits_table = {'Fresh Apple' : '62', 'Fresh Cantaloupe' : '25', 'Fresh Grapes' :'60', 'Cinnamon Apples' : '110', 'Fresh Pear' : '110', 'Fresh Banana' : '70', 'Diced Strawberries' : '120', 'Dried Cranberries' : '100', 'Diced Peaches' : '70', 'Applesauce' : '50', 'Diced Pears' : '80', 'Mixed Fruit' : '80', 'Raisins' : '130', 'Mandarin Oranges' : '80', 'Wild Blueberries' : '35', 'Baby Carrots' : '25', 'Celery Sticks' : '10', 'Broccoli Florets' : '10', 'Cucumber Slices' : '10', 'Grape Tomatoes' : '15', 'Garden Salad' : '15', 'Jicama Sticks' : '25', 'Steamed Broccoli' : '25', 'Red Peppers Strips' : '15', 'Black Charro Beans' : '130', 'Green Beans' : '20', 'Green Peas' : '70', 'Mashed Potatoes' : '80', 'Sweet Golden Corn' : '70', 'Sweet Potato Fries' : '220', 'Baked Beans' : '130'}

Button = st.button('Click me')
if Button:
    sum_food = 0
    for key, value in Fruits_table.items():
        for i in Selected:
            food = 0
            if i == key:
                food = food + int(value)
                st.write("Calorie value of", key, food)
                sum_food = sum_food + food
    st.write("Total Calorie Value: ", sum_food)

