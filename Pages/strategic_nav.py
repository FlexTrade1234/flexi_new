import streamlit as st
from Pages import home_page, predictionfactory_page, predictiongrid_page, strategicbid_page

st.sidebar.title("🎯 Strategic Bidding")

selection = st.sidebar.radio("Choose a section", [
    "Data Input Page",
    "Prediction Consumption Factory",
    "Grid Parameters Prediction",
    "Strategic Bid"
])

if selection == "Data Input Page":
    home_page.run()
elif selection == "Prediction Consumption Factory":
    predictionfactory_page.run()
elif selection == "Grid Parameters Prediction":
    predictiongrid_page.run()
elif selection == "Strategic Bid":
    strategicbid_page.run()
