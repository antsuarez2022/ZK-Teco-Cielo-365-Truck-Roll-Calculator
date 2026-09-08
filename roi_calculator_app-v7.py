import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Cielo 365 Partner ROI Calculator", 
    page_icon="⚡", 
    layout="centered"
)

# 2. Inject Custom Try.Cielo365.com Dark Slate & Corporate Orange Theme CSS
st.markdown("""
    <style>
    /* Dark Corporate Slate Background */
    .stApp {
        background: linear-gradient(180deg, #0f172a 0%, #020617 100%) !important;
        color: #f8fafc !important;
    }
    
    /* Typography Styling */
    h1, h2, h3, h4, p, label {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        color: #f8fafc !important;
    }

    /* Try.Cielo365.com Styled Header */
    .brand-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 15px 0;
        border-bottom: 1px solid #334155;
        margin-bottom: 25px;
    }
    
    .logo-text {
        font-size: 1.8rem;
        font-weight: 800;
        letter-spacing: -0.03em;
    }
    
    .logo-cielo {
        color: #ffffff !important;
    }
    
    .logo-365 {
        color: #ff6a00 !important; /* ZKTeco/Cielo Corporate Orange */
    }
    
    .tagline {
        font-size: 0.85rem;
        color: #94a3b8 !important;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        font-weight: 600;
    }

    /* Transparent Form Styling */
    div[data-testid="stForm"] {
        background-color: rgba(30, 41, 59, 0.3) !important;
        border: 1px solid #334155 !important;
        border-radius: 12px !important;
        padding: 25px !important;
    }

    /* Streamlit Slider and Widget Styling */
    div[data-testid="stSlider"] {
        padding-bottom: 10px;
    }
    
    /* Make slider labels bright and highly legible */
    div[data-testid="stWidgetLabel"] p {
        font-size: 1rem !important;
        font-weight: 500 !important;
        color: #cbd5e1 !important;
    }

    /* Input Field Customization */
    div[data-baseweb="input"] {
        background-color: #1e293b !important;
        border-radius: 8px !important;
        border: 1px solid #475569 !important;
    }
    
    input {
        color: #ffffff !important;
    }

    /* Style for Streamlit Number Input Controls (+ / - buttons) */
    button[data-testid="stNumberInputStepDown"], 
    button[data-testid="stNumberInputStepUp"] {
        background-color: #334155 !important;
        color: #ffffff !important;
        border: 1px solid #475569 !important;
        border-radius: 4px !important;
    }

    /* Form Submit (Calculate) Button Customization */
    div[data-testid="stFormSubmitButton"] button {
        background-color: #ff6a00 !important;
        color: #ffffff !important;
        border: none !important;
        padding: 10px 20px !important;
        font-weight: 700 !important;
        border-radius: 8px !important;
        width: 100% !important;
        transition: all 0.3s ease !important;
        text-transform: uppercase;
        letter-spacing: 0.03em;
    }

    div[data-testid="stFormSubmitButton"] button:hover {
        background-color: #e05d00 !important;
        box-shadow: 0 4px 15px rgba(255, 106, 0, 0.4) !important;
    }

    /* Premium Result Card Styling */
    .result-card {
        background: rgba(30, 41, 59, 0.5);
        padding: 24px;
        border-radius: 12px;
        border: 1px solid #334155;
        box-shadow: 0 4px 20px 0 rgba(0, 0, 0, 0.3);
        margin-top: 15px;
        margin-bottom: 15px;
        text-align: center;
        transition: all 0.3s ease;
    }

    .result-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 30px 0 rgba(0, 0, 0, 0.4);
    }

    .loss-card {
        border-left: 5px solid #ef4444 !important; /* Crimson Alert Red */
    }

    .savings-card {
        border-left: 5px solid #ff6a00 !important; /* Glowing Orange Brand Accent */
        background: rgba(255, 106, 0, 0.05) !important;
    }

    .cost-header {
        color: #f87171 !important;
        font-size: 0.95rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    .savings-header {
        color: #ff6a00 !important;
        font-size: 0.95rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    .value-display {
        font-size: 2.8rem;
        font-weight: 800;
        margin: 12px 0;
        color: #ffffff !important;
        letter-spacing: -0.02em;
    }

    .desc-text {
        font-size: 0.85rem;
        color: #94a3b8 !important;
        line-height: 1.4;
    }

    /* Custom Styling for the Trial Link Button */
    div.stLinkButton > a {
        background-color: transparent !important;
        color: #ff6a00 !important;
        border: 2px solid #ff6a00 !important;
        padding: 12px 24px !important;
        font-weight: 700 !important;
        border-radius: 8px !important;
        transition: all 0.3s ease !important;
        text-transform: uppercase;
        letter-spacing: 0.02em;
        display: block;
        text-align: center;
        text-decoration: none;
    }

    div.stLinkButton > a:hover {
        background-color: #ff6a00 !important;
        color: #ffffff !important;
        box-shadow: 0 6px 20px 0 rgba(255, 106, 0, 0.3) !important;
        transform: translateY(-1px);
    }
    </style>
""", unsafe_allow_html=True)

# 3. Custom Header Element
st.markdown("""
    <div class="brand-header">
        <div class="logo-text">
            <span class="logo-cielo">cielo</span><span class="logo-365">365</span>
        </div>
        <div class="tagline">Empower Access, Elevate Security</div>
    </div>
""", unsafe_allow_html=True)

# 4. Description
st.write(
    "Demonstrate the financial impact of cloud remote management. Security dealers can calculate exactly how much "
    "they protect their contract margins by transitioning from expensive physical dispatches to Cielo 365."
)

st.markdown("<br>", unsafe_allow_html=True)

# Use Streamlit Session State to persist calculation results between interactions
if 'calculated' not in st.session_state:
    st.session_state.calculated = False
    st.session_state.current_annual_cost = 0.0
    st.session_state.estimated_cloud_savings = 0.0

# 5. Interactive Configuration Form
st.markdown("### ⚙️ Partner Operations Profile")

with st.form(key="roi_form"):
    locations = st.slider(
        "How many customer locations does your business support?", 
        min_value=1, 
        max_value=150, 
        value=20,
        help="The total number of facilities or physical entry points currently under active maintenance contracts."
    )

    monthly_trips = st.slider(
        "Average physical service trips (truck rolls) per month, PER location?", 
        min_value=0, 
        max_value=10, 
        value=1,
        help="How many times a month a tech drives to a specific client site for minor adjustments or configurations."
    )

    trip_cost = st.number_input(
        "Estimated average cost per service trip ($)?", 
        min_value=50, 
        max_value=500, 
        value=150,
        step=25,
        help="The fully loaded cost of a vehicle dispatch, including fuel, technician labor rates, and vehicle overhead."
    )
    
    # Physical submit button inside the form to trigger calculation
    submit_button = st.form_submit_button(label="📊 Calculate Savings & ROI")

# 6. ROI Math Engine (Runs ONLY when the button is pressed)
if submit_button:
    st.session_state.calculated = True
    # Math scales correctly: locations * average monthly trips per location * cost per trip * 12 months
    st.session_state.current_annual_cost = float(locations * monthly_trips * trip_cost * 12)
    st.session_state.estimated_cloud_savings = float(st.session_state.current_annual_cost * 0.90)

# 7. Metrics Side-by-Side Cards (Show only after clicking 'Calculate')
if st.session_state.calculated:
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"""
            <div class="result-card loss-card">
                <div class="cost-header">📉 Current Annual Operating Loss</div>
                <div class="value-display">${st.session_state.current_annual_cost:,.0f}</div>
                <div class="desc-text">Capital lost purely to on-site vehicle travel, fuel, and technician field hours for routine configurations.</div>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
            <div class="result-card savings-card">
                <div class="savings-header">🛡️ Cielo 365 Recovered Profit</div>
                <div class="value-display">${st.session_state.estimated_cloud_savings:,.0f}</div>
                <div class="desc-text">Net annual profit recovered by diagnosing hardware, adjusting pulse times, and issuing credentials remotely.</div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # 8. Call-to-Action Link Redirect
    st.link_button(
        "🚀 Start Your Free Trial on try.cielo365.com", 
        "https://try.cielo365.com", 
        use_container_width=True
    )
else:
    st.info("💡 Enter your business parameters above and click 'Calculate Savings & ROI' to generate your custom financial breakdown.")
