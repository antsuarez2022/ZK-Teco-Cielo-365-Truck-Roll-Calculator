import streamlit as st

# Configure the page
st.set_page_config(
    page_title="ZKTeco Cielo 365 - ROI Calculator",
    page_icon="🔑",
    layout="centered"
)

# Professional branding and styling
st.markdown("""
    <style>
    .main {
        background-color: #fafafa;
    }
    .stButton>button {
        background-color: #ff9800;
        color: white;
        border-radius: 8px;
        font-weight: bold;
        height: 3em;
        width: 100%;
        border: none;
    }
    .stButton>button:hover {
        background-color: #e65100;
        color: white;
    }
    .highlight-box {
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0px;
        border-left: 5px solid #ff9800;
        background-color: #fff3e0;
    }
    </style>
""", unsafe_allow_html=True)

# Title & Description
st.title("🔑 ZKTeco Cielo 365")
st.subheader("Partner ROI Calculator: Eliminate Costly 'Truck Rolls'")
st.write(
    "When physical security dealers drive to a client's building for simple "
    "tasks (like changing a keycard or adjusting a door timer), it costs "
    "time, fuel, and labor. We call this a **'truck roll'**. "
    "Cielo 365 lets you handle these tasks **remotely** from the cloud."
)

st.markdown("---")

# Two-column layout for input and output
col_input, col_space, col_output = st.columns([1.2, 0.1, 1.2])

with col_input:
    st.markdown("### 📊 Your Business Numbers")
    
    # 1. Number of client sites
    locations = st.number_input(
        "How many client locations do you manage?",
        min_value=1,
        value=20,
        step=1,
        help="The total number of commercial offices/buildings you service."
    )
    
    # 2. Number of physical trips (truck rolls) per month
    monthly_trips = st.number_input(
        "How many service trips (truck rolls) do you make per month?",
        min_value=0,
        value=12,
        step=1,
        help="The total number of times you dispatch a technician in a vehicle to fix a minor issue."
    )
    
    # 3. Average cost per trip
    trip_cost = st.slider(
        "Average cost per service trip ($)",
        min_value=50,
        max_value=500,
        value=150,
        step=10,
        help="Includes fuel, vehicle wear-and-tear, and technician hourly wages."
    )
    
    # 4. Monthly cloud fee per location
    cielo_fee = st.number_input(
        "Estimated Cielo 365 fee per location ($/month)",
        min_value=1,
        value=10,
        step=1,
        help="Standard subscription licensing cost per cloud-connected building."
    )

# THE ROI MATH
# Current costs
current_monthly_trips_cost = monthly_trips * trip_cost
current_annual_trips_cost = current_monthly_trips_cost * 12

# Cloud-managed costs (remote diagnostics reduce routine trips by 90%)
new_monthly_trips = monthly_trips * 0.10
new_monthly_trips_cost = new_monthly_trips * trip_cost

# Total cloud platform cost
monthly_cielo_sub_cost = locations * cielo_fee
total_annual_cielo_cost = (new_monthly_trips_cost + monthly_cielo_sub_cost) * 12

# Savings
net_annual_savings = current_annual_trips_cost - total_annual_cielo_cost

with col_output:
    st.markdown("### 💰 Potential Cloud Savings")
    
    # Large metrics
    st.error(f"**Current Annual Cost of Service Trips:**  \n**${current_annual_trips_cost:,.0f}**")
    st.caption("Money lost on dispatching physical service vans for basic support.")
    
    st.info(f"**Annual Cielo 365 Cloud Investment:**  \n**${(monthly_cielo_sub_cost * 12):,.0f}**")
    st.caption("Predictable, low-cost SaaS subscription fee.")
    
    # Clear visual box for the big win
    st.markdown(
        f"""
        <div class="highlight-box">
            <h4 style="margin:0; color:#e65100;">✨ Net Annual Savings:</h4>
            <p style="font-size:28px; font-weight:bold; margin:5px 0px 0px 0px; color:#e65100;">
                ${max(0.0, net_annual_savings):,.0f} / year
            </p>
            <span style="font-size:12px; color:#555;">
                *Assumes 90% of routine settings & diagnostics are handled remotely via Cielo 365.
            </span>
        </div>
        """, 
        unsafe_allow_html=True
    )

st.markdown("---")

# Call to action
st.markdown("### Ready to stop rolling trucks and start saving?")
if st.button("🚀 Try Cielo 365 Free today at try.cielo365.com"):
    st.balloons()
    st.success("Redirecting to try.cielo365.com... (Simulated link)")
