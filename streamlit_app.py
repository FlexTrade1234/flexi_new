
import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

login_page=st.Page(
    page="Pages/login.py",
    title="Login",
    icon="👤",
    default=True
)
register_page=st.Page(
    page="Pages/register.py",
    title="Register",
    icon="📊"
)
bidding_page = st.Page(
    page="Pages/bidding.py",
    title="Submit the bids",
    icon="💸"  # Money with wings, indicating bids or money transactions
)

check_dates = st.Page(
    page="Pages/check_dates.py",
    title="Available Flexible Hours",
    icon="⏰"  # Alarm clock, indicating time for checking bidding hours
)

result_page = st.Page(
    page="Pages/result.py",
    title="Display Result",
    icon="🏆"  # Trophy, indicating results or success
)

fast1 = st.Page(
    page="Pages/fast_bid.py",
    title="Quick Bidding",
    icon="🚀",
    
)


logout=st.Page(
    page="Pages/logout.py",
    title="Logout"
)



admin1_page=st.Page(
    page="Pages/admin1.py",
    title="Market Clearance Window"
)

admin2_page=st.Page(
    page="Pages/admin2.py",
    title="Available Bids"
)


predictionfactory_page = st.Page(
    page="Pages/predictionfactory_page.py",
    title="Prediction Factory Consumption",
    icon="🏭"  # Factory icon
)

predictiongrid_page = st.Page(
    page="Pages/predictiongrid_page.py",
    title="Grid Prediction",
    icon="🔌"  # Electric plug for grid
)

strategicbid_page = st.Page(
    page="Pages/strategicbid_page.py",
    title="Strategic Bid",
    icon="🎯"  # Target icon
)

home_page = st.Page(
    page="Pages/home_page.py",
    title="Data Input Page",
    icon="🏠"  # Home icon
)

non_strategic_nav = st.Page(
    page="Pages/non_strategic_nav.py",
    title="📊 Non-Strategic Bidding"
)

strategic_nav = st.Page(
    page="Pages/strategic_nav.py",
    title="🎯 Strategic Bidding"
)




## --- NAVIGATION SETUP [WITH SECTIONS22] --- ##

if "user" in st.session_state and st.session_state["user"] == "admin":
    pg = st.navigation(
        {
            "Admin Dashboard": [admin1_page, admin2_page],
            "Account": [logout],
        }
    )

elif "user" in st.session_state:
    pg = st.navigation(
        {
            "User Dashboard": [
                home_page,
                bidding_page,
                check_dates,
                result_page,
                fast1,
            ],
            "Predictions": [
                predictionfactory_page,
                predictiongrid_page,
                strategicbid_page,
            ],
            "Account": [logout],
        }
    )

# Uncomment below if you later want separate navigation logic for different user types
# elif "user" in st.session_state:
#     pg = st.navigation(
#         {
#             "Non-Strategic": [non_strategic_nav],
#             "Strategic": [strategic_nav],
#             "Account": [logout],
#         }
#     )

else:
    pg = st.navigation(
        {
            "User Access": [login_page, register_page],
        }
    )

# Add logo to sidebar
import base64

# Load and encode the image
with open("iGRIDS.jpg", "rb") as image_file:
    encoded = base64.b64encode(image_file.read()).decode()

# Display a larger circular image in the sidebar
st.sidebar.markdown(
    f"""
    <div style="display: flex; justify-content: center; align-items: center; padding: 20px;">
        <img src="data:image/jpeg;base64,{encoded}" style="width: 200px; height: 200px; border-radius: 50%;">
    </div>
    """,
    unsafe_allow_html=True
)
if pg == login_page or pg == register_page:
# Sidebar copyright notice
    st.sidebar.markdown(
        """
        <hr style="margin-top: 30px; margin-bottom: 10px;">
        <div style="text-align: center; font-size: 12px; color: gray;">
            © 2025 iGRIDS Platform. All rights reserved.<br>
            Contact: <a href="mailto:flexiblemarket01@gmail.com">flexiblemarket01@gmail.com</a>
        </div>
        """,
        unsafe_allow_html=True
    )
#st.sidebar.image("iGRIDS.jpg", width=200)  # Adjust width as needed
#st.sidebar.image("Screenshot 2024-09-30 at 9.26.48 PM.png")
#st.sidebar.write("Please send your queries at flexiblemarket0@gmail.com by your registered email id.")
pg.run()
