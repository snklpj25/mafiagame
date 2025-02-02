import random
import streamlit as st

def assign_roles(players):
    roles = ["Mafia"] + ["Villager"] * (len(players) - 1)
    random.shuffle(roles)
    return dict(zip(players, roles))

st.title("Mafia Game")

num_players = st.number_input("Enter the number of players (4-10):", min_value=4, max_value=10, step=1)
players = []

for i in range(num_players):
    player_name = st.text_input(f"Enter name for Player {i+1}:", key=f"player_{i}")
    if player_name:
        players.append(player_name)

if len(players) == num_players:
    roles = assign_roles(players)
    st.write("Roles have been assigned. Each player should check their role privately.")
    
    for player in players:
        if st.button(f"Reveal role for {player}", key=f"reveal_{player}"):
            st.write(f"{player}, your role is: {roles[player]}")
            st.write("Keep it secret!")
