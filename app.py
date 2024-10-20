import requests
import google.generativeai as genai
import streamlit as st
from PIL import Image

# Configure Gemini API (Use your actual API key)
# genai.configure(api_key='AIzaSyD5yLv8zkGNC7YbxxODLqlMJJKTv8VWdQw')

genai.configure(api_key='AIzaSyCootL_jwKI3YDb6cKRJV-Ad0N4oKlLXXE')

# Function to get data from OpenFoodFacts API
def get_data(product_name):
    url = "https://world.openfoodfacts.org/cgi/search.pl"
    params = {
        'search_terms': product_name,
        'search_simple': 1,
        'json': 1,
    }
    response = requests.get(url, params=params)
    data = response.json()
    if 'products' not in data or len(data['products']) == 0:
        return []  # Return empty if no products found

    # Filter products with names and return top 5
    data['products'] = [p for p in data['products'] if 'product_name' in p]
    return data['products'][:1]

# Function to generate product analysis using Gemini
def generate_summary(product, tone):
    name = product.get('product_name', 'Not mentioned')
    brand = product.get('brands', 'Not mentioned')
    nutriscore_grade = product.get('nutriscore_grade', 'Not mentioned')
    eco_score = product.get('ecoscore_grade', 'Not mentioned')
    packaging = product.get('packaging', 'Not mentioned')
    ingredients = product.get('ingredients_text', 'Not mentioned')
    nutrients = product.get('nutriments', 'Not mentioned')
    nova = product.get('nova_groups_tags', 'Not mentioned')

    # Generate prompt based on tone
    prompt = f"""
    You are an AI assistant analyzing consumer products. Here are the details:
    - Name: {name}
    - Brand: {brand}
    - EcoScore: {eco_score}
    - NutriScore: {nutriscore_grade}
    - NovaScore: {nova}
    - Ingredients: {ingredients}
    - Nutrients: {nutrients}
    - Packaging: {packaging}
    Please provide a {tone} analysis including:
    1. Positive aspects of the product.
    2. Negative aspects of the product.
    3. Health impact.
    4. Environmental impact.
    """

    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text

# Streamlit interface
def main():
    # Page setup and header with background image
    st.set_page_config(page_title="ConsumeNice", page_icon="🍽", layout="centered")

    # Custom CSS for better aesthetics
    st.markdown(
        """
        <style>
        .main {background-color: #000000;}
        .reportview-container .main .block-container {
            padding-top: 2rem;
            padding-right: 2.5rem;
            padding-left: 2.5rem;
        }
        h1, h2, h3, h4, h5 {color: #ffffff;}
        .stButton>button {
            background-color: #6c757d; 
            color: white;
            border-radius: 8px;
        }
        .stButton>button:hover {
            background-color: #5a6268;
        }
        .stTextInput>div>input {
            padding: 10px; 
            border-radius: 6px; 
            border: 1px solid #ced4da;
            background-color: #f8f9fa;
        }
        .stRadio>div>label {color: #495057 !important;}
        .css-1d391kg {color: #495057 !important;}
        .css-145kmo2 {color: #495057 !important;}
        </style>
        """, 
        unsafe_allow_html=True
    )

    # App logo and header side by side
    col1, col2 = st.columns([1, 3])  # Adjust proportions as needed
    with col1:
        st.image(Image.open('logo.png'), width=120, caption="ConsumeNice - Know What You Consume")
    with col2:
        st.markdown(
            "<h1 style='text-align: left; color: #ffffff;'>🍽️ ConsumeNice - Analyze Products with AI</h1>", 
            unsafe_allow_html=True
        )

    st.write("Welcome to ConsumeNice, where you can search for products and get an AI-generated analysis based on their nutritional, environmental, and packaging details.")
    
    # Sidebar for developer profiles and hackathon info
    st.sidebar.markdown(
        """
        <h1 style='color: #0072B2;'>🚀 Hackathon Project</h1>
        """, 
        unsafe_allow_html=True
    )
    st.sidebar.markdown("Welcome to the ConsumeNice project, developed for the hackathon to showcase AI integration in product analysis.")

    # Add some icons/emojis to make it look more engaging
    st.sidebar.markdown("### 🔧 Project Features")
    # st.sidebar.markdown("- Analyze product details using OpenFoodFacts API.")
    st.sidebar.markdown("- AI-generated analysis using Google Gemini AI.")
    st.sidebar.markdown("- Environment, packaging, and health analysis.")

    # Developer details with LinkedIn links
    st.sidebar.markdown("### 👨‍💻 Developers")
    st.sidebar.markdown("[Srish](https://www.linkedin.com/in/srishrachamalla/) - AI/ML Developer")
    st.sidebar.markdown("[Sai Teja](https://www.linkedin.com/in/saiteja-pallerla-668734225/) - Data Analyst")

    # Add expander sections for additional content
    with st.sidebar.expander("ℹ About ConsumeNice"):
        st.write("ConsumeNice is designed to give consumers more insights into the products they consume, analyzing factors like health impact, environmental footprint, and packaging.")

    with st.sidebar.expander("📚 Useful Resources"):
        st.write("[Google Gemini AI Documentation](https://ai.google.dev/gemini-api/docs)")
        st.write("[Streamlit Documentation](https://docs.streamlit.io/)")

    # Add progress indicator for hackathon phases or development stages
    st.sidebar.markdown("### ⏳ Hackathon Progress")
    st.sidebar.progress(0.99)  # Set progress level (0 to 1)

    # Sidebar footer with final notes
    st.sidebar.markdown("---")
    st.sidebar.markdown(
        """
        <div style="text-align: center; font-size: 0.85em;">
            Developed by Srish & Sai Teja • Powered by Google Gemini AI
        </div>
        """, unsafe_allow_html=True
    )

    # User input fields with improved placeholders and hints
    product_input = st.text_input("Enter Product Name", placeholder="e.g., Coca-Cola, Oreo, Dove Soap")
    tone = st.radio("Choose Analysis Depth", options=["Simple", "In-depth"], index=0)

#     ##ss
    if st.button("Search"):
        with st.spinner("Searching for products..."):
            products = get_data(product_input)
        
        if not products:
            st.error("No products found for the given name.")
        else:
            # product_names = [f"{p['product_name']} (Brand: {p.get('brands', 'Unknown')})" for p in products]
            # selected_product_name = st.radio("Select a Product", product_names, key='product_selection')
            # print(selected_product_name)

            # selected_product = next(p for p in products if f"{p['product_name']} (Brand: {p.get('brands', 'Unknown')})" == selected_product_name)
            # print(selected_product)

            # st.write(f"### Product Selected: {selected_product['product_name']} (Brand: {selected_product.get('brands', 'Unknown')})")

            # if selected_product:
            #     if 'summary' not in st.session_state:
            #         st.session_state.summary = None

            #     with st.spinner("Generating AI-powered analysis..."):
            #         summary = generate_summary(selected_product, tone.lower())
            #     st.session_state.summary = summary

            #     st.write("### Product Analysis Summary:")
            #     st.success(st.session_state.summary)
            product_names = [f"{p['product_name']} (Brand: {p.get('brands', 'Unknown')})" for p in products]
            selected_product = products[0]
            st.write(f"### Product Selected: {product_names[0]}")
            with st.spinner("Generating AI-powered analysis..."):
                    summary = generate_summary(selected_product, tone.lower())
            st.session_state.summary = summary

            st.write("### Product Analysis Summary:")
            st.success(st.session_state.summary)
            
    

    # Footer with hackathon and design details
    st.markdown("---")
    st.markdown("""
        <div style="text-align: center; font-size: 0.9em;">
        <p><i>ConsumeNice</i> was developed for a hackathon using <b>Streamlit</b> to showcase AI integration with real-world data sources.</p>
        <p>Developed by Srish & Sai Teja • Powered by Google Gemini AI</p>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()