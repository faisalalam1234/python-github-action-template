import streamlit as st
import time

# Set page title and layout with Amazon Icon
st.set_page_config(page_title="EMI Calculator", page_icon="https://upload.wikimedia.org/wikipedia/commons/d/de/Amazon_icon.png", layout="wide")

# Responsive CSS for mobile-friendly layout
st.markdown(
    """
    <style>
        .responsive-banner {
            text-align: center;
            margin-bottom: 20px;
        }
        .responsive-banner img {
            max-width: 100%; 
            height: auto; 
        }
        @media (max-width: 600px) {
            .responsive-banner img {
                width: 100% !important;
                height: auto !important;
            }
            .streamlit-expanderHeader {
                font-size: 16px;
            }
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Create a slider (Selectbox) for navigation
page = st.radio(
    "Navigate to:",
    ("Home", "About Us", "Contact Us")
)

if page == "Home":
    # Home page content
    st.markdown(
        """
        <div class="responsive-banner">
            <a href="https://amzn.to/4ijUaFU" target="_blank">
                <img src="https://images-eu.ssl-images-amazon.com/images/G/31/img16/vineet/Amazon-Pay-Later/Nov_21/3_month_NCEMI/770x250.jpg" alt="Amazon Pay Later Offer" />
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    # Title and basic intro
    st.title("EMI Calculator with Amazon Pay Later")
    st.subheader("Calculate your loan EMI and learn more about Amazon Pay Later!")

    # Input fields for loan calculation
    loan_amount = st.number_input(
        "Enter Loan Amount (₹)", min_value=1000, max_value=1000000, step=1000, value=10000
    )
    annual_interest_rate = st.number_input(
        "Enter Annual Interest Rate (%)", min_value=0.1, max_value=50.0, step=0.1, value=5.0
    )
    loan_tenure_years = st.number_input(
        "Enter Loan Tenure (Years)", min_value=1, max_value=30, step=1, value=1
    )

    # EMI calculation formula
    def calculate_emi(principal, annual_rate, years):
        monthly_rate = (annual_rate / 100) / 12
        months = years * 12
        emi = (principal * monthly_rate * (1 + monthly_rate) ** months) / (
            (1 + monthly_rate) ** months - 1
        )
        return emi

    # Button to trigger calculation
    if st.button("Calculate EMI"):
        # Show progress bar
        with st.spinner("Calculating EMI..."):
            progress = st.progress(0)
            for i in range(100):
                time.sleep(0.02)  # Simulate delay for user experience
                progress.progress(i + 1)

        # Calculate EMI
        emi = calculate_emi(loan_amount, annual_interest_rate, loan_tenure_years)

        # Display the result
        st.success("Calculation Complete!")
        st.write(f"### Your Monthly EMI: ₹{emi:.2f}")

    # Offer Details Section
    st.markdown(
        """
        ## Why Choose Amazon Pay Later?
        Amazon Pay Later allows you to shop now and pay later in easy EMIs.
        With minimal paperwork and easy-to-use features, you can manage your expenses effortlessly. 
        **Click the banner above to learn more and apply today!**
        """
    )

    # Payment Details Section
    st.markdown(
        """
        ## About Amazon Pay Later
        Amazon Pay Later is a great way to make purchases on Amazon and other partner sites. 
        The EMI feature is available on all eligible products, making it simple to pay in installments.

        **How does it work?**
        - Instant approval.
        - Flexible EMI plans.
        - Simple application process.

        Don't wait! Start your Amazon Pay Later journey today!
        """
    )

    # Add GIF Banner at the bottom with a link
    st.markdown(
        """
        <div class="responsive-banner">
            <a href="https://amzn.to/4ijUaFU" target="_blank">
                <img src="https://media.giphy.com/media/3o7TKt7c5FfTf5X70w/giphy.gif" alt="Amazon Pay Later GIF" />
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )

elif page == "About Us":
    # About Us content
    st.header("About Us")
    st.write(
        """
        My Name Is Faisal Alam I AM From India - Uttar Pradesh 
        We are dedicated to providing financial solutions that help people make smart purchasing decisions. 
        Amazon Pay Later makes it easier to buy today and pay later in easy EMIs with minimal paperwork.
        """
    )

elif page == "Contact Us":
    # Contact Us content
    st.header("Contact Us")
    st.write(
        """
        For any inquiries, you can reach us at:
        
        - Email: ka9190430@gmail..com
        - Phone: +91 9219711509
        """
    )
