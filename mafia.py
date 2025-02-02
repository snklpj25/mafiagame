import streamlit as st
import random
import uuid

def assign_roles(players):
    mafia = random.choice(players)
    roles = {player: "Mafia" if player == mafia else "Villager" for player in players}
    return roles

def generate_unique_links(players):
    links = {player: f"/role/{uuid.uuid4()}" for player in players}
    return links

st.title("Mafia Chit Game")

st.write("Enter player names to assign roles.")

player_count = st.number_input("Number of Players (Min: 3, Max: 10)", min_value=3, max_value=10, step=1)
players = []

for i in range(player_count):
    player_name = st.text_input(f"Player {i+1} Name", "")
    if player_name:
        players.append(player_name)

if st.button("Assign Roles"):
    if len(players) < 3:
        st.error("At least 3 players are required.")
    else:
        roles = assign_roles(players)
        links = generate_unique_links(players)
        st.session_state["roles"] = roles
        st.session_state["links"] = links
        st.success("Roles have been assigned. Each player has a unique link to reveal their role.")

if "roles" in st.session_state:
    st.write("Share these unique links with each player to reveal their role privately:")
    for player, link in st.session_state["links"].items():
        st.write(f"{player}: [Click to reveal role]({link})")
