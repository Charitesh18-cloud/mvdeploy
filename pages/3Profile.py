# pages/3_Profile.py
import streamlit as st

st.title("👤 Your Profile")

xp = st.session_state.get("xp", 0)
streak = st.session_state.get("streak", 1)

st.write("*Name:* Guest User")
st.write(f"*XP Points:* {xp}")
st.write(f"*Current Streak:* {streak}")

st.progress(min(xp % 100, 100), text="XP Progress")