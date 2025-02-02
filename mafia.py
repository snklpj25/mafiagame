import streamlit as st
import pywhatkit as kit
import time
import random

def send_message(phone_number, message):
    try:
        kit.sendwhatmsg_instantly(phone_number, message, wait_time=10, tab_close=True, close_time=5)
        st.success(f"Message sent to {phone_number}: {message}")
    except Exception as e:
        st.error(f"Failed to send message to {phone_number}: {str(e)}")

st.title("Mafia Game - WhatsApp Message Sender")

st.write("Enter up to 5 phone numbers (including country code) to assign roles randomly.")

phone_numbers = []
for i in range(5):
    phone_number = st.text_input(f"Phone number {i+1} (optional)", "")
    if phone_number:
        phone_numbers.append(phone_number)

if st.button("Assign Roles and Send Messages"):
    if len(phone_numbers) < 2:
        st.error("Enter at least 2 phone numbers.")
    else:
        mafia = random.choice(phone_numbers)
        for num in phone_numbers:
            role = "Mafia" if num == mafia else "Villager"
            send_message(num, f"Your assigned role is: {role}")
        st.success("Messages sent successfully!")
