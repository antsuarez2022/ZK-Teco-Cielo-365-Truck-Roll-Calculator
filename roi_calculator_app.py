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

    /* Custom Styling for the Call-to-Action Link Button */
    div.stLinkButton > a {
        background-color: #ff6a00 !important;
        color: #ffffff !important;
        border: none !important;
        padding: 12px 24px !important;
        font-weight: 700 !important;
        border-radius: 8px !important;
        box-shadow: 0 4px 14px 0 rgba(255, 106, 0, 0.3) !important;
        transition: all 0.3s ease !important;
        text-transform: uppercase;
        letter-spacing: 0.02em;
    }

    div.stLinkButton > a:hover {
        background-color: #e05d00 !important;
        box-shadow: 0 6px 20px 0 rgba(255, 106, 0, 0.5) !important;
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
    "they protect their contract margins by transitioning from expensive physical dispatches ('truck rolls') "
    "to Cielo 365 [cite: 52, 57]."
)

st.markdown("<br>", unsafe_allow_html=True)

# 5. Interactive Configuration Inputs
st.markdown("### ⚙️ Partner Operations Profile")

locations = st.slider(
    "How many customer locations does your business support?", 
    min_value=1, 
    max_value=150, 
    value=20,
    help="The total number of facilities or physical entry points currently under active maintenance contracts."
)

monthly_trips = st.slider(
    "Average number of physical service trips (truck rolls) per month?", 
    min_value=0, 
    max_value=100, 
    value=15,
    help="How many times a month a tech must drive to a client site for minor adjustments, badge enrollments, or door schedules [cite: 47, 57]."
)

trip_cost = st.number_input(
    "Estimated average cost per service trip ($)?", 
    min_value=50, 
    max_value=500, 
    value=150,
    step=25,
    help="The fully loaded cost of a vehicle dispatch, including fuel, technician labor rates, and vehicle overhead. Standard industry benchmarks are $150–$300+ ."
)

# 6. ROI Math Engine
# Remote cloud management eliminates up to 90% of physical service dispatches by enabling cloud configuration
current_annual_cost = monthly_trips * trip_cost * 12
estimated_cloud_savings = current_annual_cost * 0.90 

# 7. Metrics Side-by-Side Cards
st.markdown("<br>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
        <div class="result-card loss-card">
            <div class="cost-header">Current Annual Operating Loss</div>
            <div class="value-display">$ [cite: 57]{current_annual_cost:,.0f}</div>
            <div class="desc-text">Capital lost purely to on-site vehicle travel, fuel, and technician field hours for routine configurations [cite: 57].</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class="result-card savings-card">
            <div class="savings-header">Cielo 365 Recovered Profit</div>
            <div class="value-display">${estimated_cloud_savings:,.0f}</div>
            <div class="desc-text">Net annual profit recovered by diagnosing hardware, adjusting pulse times, and issuing credentials remotely [cite: 47, 52].</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 8. Fixed Call-to-Action Link Redirect (Corporate Orange Hover, Opens in New Tab)
st.link_button(
    "🚀 Start Your Free Trial on try.cielo365.com", 
    "https://try.cielo365.com", 
    use_container_width=True
)
