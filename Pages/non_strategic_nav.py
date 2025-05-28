import streamlit as st
from Pages import bidding, check_dates, result, fast_bid  # your modules

st.sidebar.title("📊 Non-Strategic Bidding")

selection = st.sidebar.radio("Choose a section", [
    "Submit the bids",
    "Available Flexible Hours",
    "Display Result",
    "Fast_Bidding"
])

if selection == "Submit the bids":
    bidding.run()  # Function from bidding.py
elif selection == "Available Flexible Hours":
    check_dates.run()
elif selection == "Display Result":
    result.run()
elif selection == "Fast_Bidding":
    fast_bid.run()
