import streamlit as st
import pandas as pd
from datetime import datetime

# Sample data for available gifts
gifts = [
    {"name": "Flowers", "price": 20},
    {"name": "Chocolates", "price": 15},
    {"name": "Gadgets", "price": 200},
    {"name": "Personalized Mug", "price": 10},
    {"name": "Books", "price": 25},
]

# Function to display gift options
def display_gift_options():
    selected_gift = st.selectbox("Select a gift", [gift['name'] for gift in gifts])
    gift_price = next(gift['price'] for gift in gifts if gift['name'] == selected_gift)
    st.write(f"Price: ${gift_price}")
    return selected_gift, gift_price

# Main app function
def main():
    st.title("Saprembhet - Gift Delivery Service")
    
    # Sender and Receiver information
    st.header("Sender Information")
    sender_name = st.text_input("Sender's Name")
    sender_address = st.text_input("Sender's Address")
    
    st.header("Receiver Information")
    receiver_name = st.text_input("Receiver's Name")
    receiver_address = st.text_input("Receiver's Address")
    
    # Select a gift
    st.header("Select a Gift")
    selected_gift, gift_price = display_gift_options()
    
    # Personalized note
    st.header("Personalized Note")
    note = st.text_area("Write a personalized note to attach with the gift")

    # Desired delivery time
    st.header("Delivery Details")
    delivery_date = st.date_input("Select desired delivery date", min_value=datetime.today())
    delivery_time = st.time_input("Select desired delivery time")
    
    # Live location tracking simulation (For demonstration purposes)
    st.header("Track your Gift")
    if st.button("Start Tracking"):
        st.write("Tracking started... Your gift is on the way!")
        st.map()
    
    # Order summary and confirmation
    st.header("Order Summary")
    if st.button("Confirm Order"):
        st.success("Order confirmed!")
        st.write(f"**Sender:** {sender_name}, {sender_address}")
        st.write(f"**Receiver:** {receiver_name}, {receiver_address}")
        st.write(f"**Gift:** {selected_gift}, ${gift_price}")
        st.write(f"**Note:** {note}")
        st.write(f"**Delivery Date & Time:** {delivery_date} at {delivery_time}")

if __name__ == "__main__":
    main()
