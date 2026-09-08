import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Cielo 365 ROI Calculator", 
    page_icon="💜", 
    layout="centered"
)

# 2. Inject Custom Vibrant Purple Theme CSS
st.markdown("""
    <style>
    /* Gradient Background for the Entire App */
    .stApp {
        background: linear-gradient(135deg, #1e0b36 0%, #090212 100%) !important;
        color: #f3ebff !important;
    }
    
    /* Global Text Styling */
    h1, h2, h3, h4, p, label {
        font-family: 'Inter', 'Helvetica Neue', sans-serif;
        color: #f3ebff !important;
    }

    /* Input Field Customization */
    div[data-baseweb="input"] {
        background-color: #2d124d !important;
        border-radius: 10px !important;
        border: 1px solid #9d4edd !important;
        color: #ffffff !important;
    }
    
    input {
        color: #ffffff !important;
    }

    /* Style for Streamlit Number Input Controls (+ / - buttons) */
    button[data-testid="stNumberInputStepDown"], 
    button[data-testid="stNumberInputStepUp"] {
        background-color: #3c1e63 !important;
        color: #ffffff !important;
        border: 1px solid #9d4edd !important;
        border-radius: 5px !important;
    }

    /* Container Styling for Results Cards */
    .result-card {
        background: rgba(45, 18, 77, 0.45);
        padding: 24px;
        border-radius: 16px;
        border: 1px solid #9d4edd;
        box-shadow: 0 8px 32px 0 rgba(157, 78, 221, 0.2);
        margin-top: 15px;
        margin-bottom: 15px;
        text-align: center;
    }

    .cost-header {
        color: #ff6b8b !important;
        font-size: 1.1rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    .savings-header {
        color: #2ecc71 !important;
        font-size: 1.1rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    .value-display {
        font-size: 2.5rem;
        font-weight: 800;
        margin: 12px 0;
        color: #ffffff !important;
    }

    .desc-text {
        font-size: 0.9rem;
        color: #d1bbf2 !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Header & Introduction
st.title("💜 Cielo 365 Partner ROI Calculator")
st.write(
    "Calculate how much your physical security dealership can save by shifting "
    "from high-cost physical dispatches ('truck rolls') to remote cloud access control."
)

st.markdown("---")

# 4. Interactive Input Sliders (Low Friction)
st.subheader("⚙️ Enter Your Business Numbers")

locations = st.slider(
    "How many customer locations do you manage?", 
    min_value=1, 
    max_value=100, 
    value=15,
    help="The total number of building entry systems or controller panels you support."
)

monthly_trips = st.slider(
    "Average service trips (truck rolls) per month?", 
    min_value=0, 
    max_value=50, 
    value=10,
    help="How many times a technician drives a van out to handle minor configs, credential issues, or diagnostics."
)

trip_cost = st.number_input(
    "Average cost per physical service trip ($)?", 
    min_value=50, 
    max_value=500, 
    value=150,
    step=25,
    help="Standard industry truck rolls cost between $150 and $300+ in fuel, wear, and labor."
)

# 5. Core ROI Math
# Cielo 365 cloud-based remote management can reduce physical maintenance trips by up to 90%
current_annual_cost = monthly_trips * trip_cost * 12
estimated_cloud_savings = current_annual_cost * 0.90 

# 6. Side-by-Side Visual Cards
st.markdown("<br>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
        <div class="result-card" style="border-color: #ff3366;">
            <div class="cost-header">Current Annual Loss</div>
            <div class="value-display">${current_annual_cost:,.0f}</div>
            <div class="desc-text">Spent annually on truck dispatches, fuel, and technician field labor.</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class="result-card" style="border-color: #2ecc71;">
            <div class="savings-header">Cielo 365 Net Savings</div>
            <div class="value-display">${estimated_cloud_savings:,.0f}</div>
            <div class="desc-text">Retained profits by resolving up to 90% of service issues remotely.</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 7. Redirection Link Button (Fixed to prevent page refresh loop!)
st.link_button(
    "🚀 Start Saving Today — Try Cielo 365 Free", 
    "https://try.cielo365.com", 
    use_container_width=True
)
