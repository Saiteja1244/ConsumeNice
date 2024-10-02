# # # # # # import requests
# # # # # # import google.generativeai as genai
# # # # # # import streamlit as st

# # # # # # # Configure Gemini API (Use your actual API key)
# # # # # # genai.configure(api_key='AIzaSyD5yLv8zkGNC7YbxxODLqlMJJKTv8VWdQw')

# # # # # # # Function to get data from OpenFoodFacts API
# # # # # # def get_data(product_name):
# # # # # #     url = "https://world.openfoodfacts.org/cgi/search.pl"
# # # # # #     params = {
# # # # # #         'search_terms': product_name,
# # # # # #         'search_simple': 1,
# # # # # #         'json': 1,
# # # # # #     }
# # # # # #     response = requests.get(url, params=params)
# # # # # #     data = response.json()
# # # # # #     if 'products' not in data or len(data['products']) == 0:
# # # # # #         return []  # Return empty if no products found

# # # # # #     # Filter products with names and return top 5
# # # # # #     data['products'] = [p for p in data['products'] if 'product_name' in p]
# # # # # #     return data['products'][:5]

# # # # # # # Function to generate product analysis using Gemini
# # # # # # def generate_summary(product, tone):
# # # # # #     name = product.get('product_name', 'Not mentioned')
# # # # # #     brand = product.get('brands', 'Not mentioned')
# # # # # #     nutriscore_grade = product.get('nutriscore_grade', 'Not mentioned')
# # # # # #     eco_score = product.get('ecoscore_grade', 'Not mentioned')
# # # # # #     packaging = product.get('packaging', 'Not mentioned')
# # # # # #     ingredients = product.get('ingredients_text', 'Not mentioned')
# # # # # #     nutrients = product.get('nutriments', 'Not mentioned')
# # # # # #     nova = product.get('nova_groups_tags', 'Not mentioned')

# # # # # #     # Generate prompt based on tone
# # # # # #     prompt = f"""
# # # # # #     You are an AI assistant analyzing consumer products. Here are the details:
# # # # # #     - Name: {name}
# # # # # #     - Brand: {brand}
# # # # # #     - EcoScore: {eco_score}
# # # # # #     - NutriScore: {nutriscore_grade}
# # # # # #     - NovaScore: {nova}
# # # # # #     - Ingredients: {ingredients}
# # # # # #     - Nutrients: {nutrients}
# # # # # #     - Packaging: {packaging}

# # # # # #     Please provide a {tone} analysis including:
# # # # # #     1. Positive aspects of the product.
# # # # # #     2. Negative aspects of the product.
# # # # # #     3. Health impact.
# # # # # #     4. Environmental impact.
# # # # # #     """
    
# # # # # #     model = genai.GenerativeModel(model_name="gemini-1.5-flash")
# # # # # #     response = model.generate_content(prompt)
# # # # # #     return response.text

# # # # # # # Streamlit Interface
# # # # # # def main():
# # # # # #     st.title("ConsumeNice")
# # # # # #     st.write("Get product details and summaries using OpenFoodFacts and Gemini AI.")

# # # # # #     product_name = st.text_input("Enter the product name:")
# # # # # #     tone = st.radio("Select the tone for the analysis:", options=["simple", "deeper"], index=0)

# # # # # #     if st.button("Search"):
# # # # # #         products = get_data(product_name)
# # # # # #         if not products:
# # # # # #             st.write("No products found for the given name.")
# # # # # #         else:
# # # # # #             product_options = [f"{p['product_name']} (Brand: {p.get('brands', 'Unknown')})" for p in products]
# # # # # #             selected_product_name = st.selectbox("Select a Product", product_options)

# # # # # #             # Get the selected product
# # # # # #             selected_product = next((p for p in products if selected_product_name.startswith(p['product_name'])), None)

# # # # # #             if selected_product:
# # # # # #                 summary = generate_summary(selected_product, tone)
# # # # # #                 st.write(f"### Product Name: {selected_product['product_name']} (Brand: {selected_product.get('brands', 'Unknown')})")
# # # # # #                 st.write(summary)
# # # # # #             else:
# # # # # #                 st.write("Selected product not found.")

# # # # # # if __name__ == "__main__":
# # # # # #     main()
# # # # # import requests
# # # # # import google.generativeai as genai
# # # # # import streamlit as st

# # # # # # Configure Gemini API (Use your actual API key)
# # # # # genai.configure(api_key='AIzaSyD5yLv8zkGNC7YbxxODLqlMJJKTv8VWdQw')

# # # # # # Function to get data from OpenFoodFacts API
# # # # # def get_data(product_name):
# # # # #     url = "https://world.openfoodfacts.org/cgi/search.pl"
# # # # #     params = {
# # # # #         'search_terms': product_name,
# # # # #         'search_simple': 1,
# # # # #         'json': 1,
# # # # #     }
# # # # #     response = requests.get(url, params=params)
# # # # #     data = response.json()
# # # # #     if 'products' not in data or len(data['products']) == 0:
# # # # #         return []  # Return empty if no products found

# # # # #     # Filter products with names and return top 5
# # # # #     data['products'] = [p for p in data['products'] if 'product_name' in p]
# # # # #     return data['products'][:5]

# # # # # # Function to generate product analysis using Gemini
# # # # # def generate_summary(product, tone):
# # # # #     name = product.get('product_name', 'Not mentioned')
# # # # #     brand = product.get('brands', 'Not mentioned')
# # # # #     nutriscore_grade = product.get('nutriscore_grade', 'Not mentioned')
# # # # #     eco_score = product.get('ecoscore_grade', 'Not mentioned')
# # # # #     packaging = product.get('packaging', 'Not mentioned')
# # # # #     ingredients = product.get('ingredients_text', 'Not mentioned')
# # # # #     nutrients = product.get('nutriments', 'Not mentioned')
# # # # #     nova = product.get('nova_groups_tags', 'Not mentioned')

# # # # #     # Generate prompt based on tone
# # # # #     prompt = f"""
# # # # #     You are an AI assistant analyzing consumer products. Here are the details:
# # # # #     - Name: {name}
# # # # #     - Brand: {brand}
# # # # #     - EcoScore: {eco_score}
# # # # #     - NutriScore: {nutriscore_grade}
# # # # #     - NovaScore: {nova}
# # # # #     - Ingredients: {ingredients}
# # # # #     - Nutrients: {nutrients}
# # # # #     - Packaging: {packaging}

# # # # #     Please provide a {tone} analysis including:
# # # # #     1. Positive aspects of the product.
# # # # #     2. Negative aspects of the product.
# # # # #     3. Health impact.
# # # # #     4. Environmental impact.
# # # # #     """
    
# # # # #     model = genai.GenerativeModel(model_name="gemini-1.5-flash")
# # # # #     response = model.generate_content(prompt)
# # # # #     return response.text

# # # # # # Streamlit UI
# # # # # def app():
# # # # #     st.title("ConsumeNice Product Analyzer")
    
# # # # #     product_name = st.text_input("Enter Product Name", "")
# # # # #     tone = st.radio("Summary Tone", ["simple", "deeper"], index=0)
    
# # # # #     if st.button("Search Products"):
# # # # #         products = get_data(product_name)
        
# # # # #         if not products:
# # # # #             st.write("No products found for the given name.")
# # # # #             return
        
# # # # #         product_names = [f"{p['product_name']} (Brand: {p.get('brands', 'Unknown')})" for p in products]
        
# # # # #         # Dropdown for selecting a product
# # # # #         selected_product_name = st.selectbox("Select a Product", product_names)
        
# # # # #         # Once a product is selected, find the corresponding product data
# # # # #         selected_product = next((p for p in products if selected_product_name.split(' (Brand: ')[0] == p['product_name']), None)
        
# # # # #         if selected_product:
# # # # #             st.write(f"Generating summary for: {selected_product['product_name']}")
# # # # #             summary = generate_summary(selected_product, tone)
# # # # #             st.write(summary)

# # # # # if __name__ == "__main__":
# # # # #     app()
# # # # import requests
# # # # import google.generativeai as genai
# # # # import streamlit as st

# # # # # Configure Gemini API (Use your actual API key)
# # # # genai.configure(api_key='AIzaSyD5yLv8zkGNC7YbxxODLqlMJJKTv8VWdQw')

# # # # # Function to get data from OpenFoodFacts API
# # # # def get_data(product_name):
# # # #     url = "https://world.openfoodfacts.org/cgi/search.pl"
# # # #     params = {
# # # #         'search_terms': product_name,
# # # #         'search_simple': 1,
# # # #         'json': 1,
# # # #     }
# # # #     response = requests.get(url, params=params)
# # # #     data = response.json()
# # # #     if 'products' not in data or len(data['products']) == 0:
# # # #         return []  # Return empty if no products found

# # # #     # Filter products with names and return top 5
# # # #     data['products'] = [p for p in data['products'] if 'product_name' in p]
# # # #     return data['products'][:5]

# # # # # Function to generate product analysis using Gemini
# # # # def generate_summary(product, tone):
# # # #     name = product.get('product_name', 'Not mentioned')
# # # #     brand = product.get('brands', 'Not mentioned')
# # # #     nutriscore_grade = product.get('nutriscore_grade', 'Not mentioned')
# # # #     eco_score = product.get('ecoscore_grade', 'Not mentioned')
# # # #     packaging = product.get('packaging', 'Not mentioned')
# # # #     ingredients = product.get('ingredients_text', 'Not mentioned')
# # # #     nutrients = product.get('nutriments', 'Not mentioned')
# # # #     nova = product.get('nova_groups_tags', 'Not mentioned')

# # # #     # Generate prompt based on tone
# # # #     prompt = f"""
# # # #     You are an AI assistant analyzing consumer products. Here are the details:
# # # #     - Name: {name}
# # # #     - Brand: {brand}
# # # #     - EcoScore: {eco_score}
# # # #     - NutriScore: {nutriscore_grade}
# # # #     - NovaScore: {nova}
# # # #     - Ingredients: {ingredients}
# # # #     - Nutrients: {nutrients}
# # # #     - Packaging: {packaging}

# # # #     Please provide a {tone} analysis including:
# # # #     1. Positive aspects of the product.
# # # #     2. Negative aspects of the product.
# # # #     3. Health impact.
# # # #     4. Environmental impact.
# # # #     """

# # # #     model = genai.GenerativeModel(model_name="gemini-1.5-flash")
# # # #     response = model.generate_content(prompt)
# # # #     return response.text

# # # # # Streamlit interface
# # # # def main():
# # # #     st.title("ConsumeNice")
# # # #     st.write("Get product details and summaries using OpenFoodFacts and Gemini AI.")

# # # #     product_input = st.text_input("Product Name", placeholder="Enter the product name...")
# # # #     tone = st.radio("Summary Tone", options=["simple", "deeper"], index=0)

# # # #     if st.button("Search"):
# # # #         products = get_data(product_input)
# # # #         if not products:
# # # #             st.error("No products found for the given name.")
# # # #         else:
# # # #             product_names = [f"{p['product_name']} (Brand: {p.get('brands', 'Unknown')})" for p in products]
# # # #             selected_product_name = st.selectbox("Select a Product", product_names)

# # # #             # Find the selected product details
# # # #             selected_product = next(p for p in products if f"{p['product_name']} (Brand: {p.get('brands', 'Unknown')})" == selected_product_name)
# # # #             print(selected_product)

# # # #             if selected_product:
# # # #                 summary = generate_summary(selected_product, tone)
# # # #                 st.write(f"### Summary for: {selected_product['product_name']} (Brand: {selected_product.get('brands', 'Unknown')})")
# # # #                 st.write(summary)

# # # # if __name__ == "__main__":
# # # #     main()
# # # import requests
# # # import google.generativeai as genai
# # # import streamlit as st
# # # import time

# # # # Configure Gemini API (Use your actual API key)
# # # genai.configure(api_key='AIzaSyD5yLv8zkGNC7YbxxODLqlMJJKTv8VWdQw')

# # # # Function to get data from OpenFoodFacts API
# # # def get_data(product_name):
# # #     url = "https://world.openfoodfacts.org/cgi/search.pl"
# # #     params = {
# # #         'search_terms': product_name,
# # #         'search_simple': 1,
# # #         'json': 1,
# # #     }
# # #     response = requests.get(url, params=params)
# # #     data = response.json()
# # #     if 'products' not in data or len(data['products']) == 0:
# # #         return []  # Return empty if no products found

# # #     # Filter products with names and return top 5
# # #     data['products'] = [p for p in data['products'] if 'product_name' in p]
# # #     return data['products'][:5]

# # # # Function to generate product analysis using Gemini
# # # def generate_summary(product, tone):
# # #     name = product.get('product_name', 'Not mentioned')
# # #     brand = product.get('brands', 'Not mentioned')
# # #     nutriscore_grade = product.get('nutriscore_grade', 'Not mentioned')
# # #     eco_score = product.get('ecoscore_grade', 'Not mentioned')
# # #     packaging = product.get('packaging', 'Not mentioned')
# # #     ingredients = product.get('ingredients_text', 'Not mentioned')
# # #     nutrients = product.get('nutriments', 'Not mentioned')
# # #     nova = product.get('nova_groups_tags', 'Not mentioned')

# # #     # Generate prompt based on tone
# # #     prompt = f"""
# # #     You are an AI assistant analyzing consumer products. Here are the details:
# # #     - Name: {name}
# # #     - Brand: {brand}
# # #     - EcoScore: {eco_score}
# # #     - NutriScore: {nutriscore_grade}
# # #     - NovaScore: {nova}
# # #     - Ingredients: {ingredients}
# # #     - Nutrients: {nutrients}
# # #     - Packaging: {packaging}

# # #     Please provide a {tone} analysis including:
# # #     1. Positive aspects of the product.
# # #     2. Negative aspects of the product.
# # #     3. Health impact.
# # #     4. Environmental impact.
# # #     """

# # #     model = genai.GenerativeModel(model_name="gemini-1.5-flash")
# # #     response = model.generate_content(prompt)
# # #     return response.text

# # # # Streamlit interface
# # # def main():
# # #     st.title("ConsumeNice")
# # #     st.write("Get product details and summaries using OpenFoodFacts and Gemini AI.")

# # #     product_input = st.text_input("Product Name", placeholder="Enter the product name...")
# # #     tone = st.radio("Summary Tone", options=["simple", "deeper"], index=0)

# # #     if st.button("Search"):
# # #         products = get_data(product_input)
# # #         if not products:
# # #             st.error("No products found for the given name.")
# # #         else:
# # #             product_names = [f"{p['product_name']} (Brand: {p.get('brands', 'Unknown')})" for p in products]
# # #             selected_product_name = st.radio("Select a Product", product_names)
# # #             time.sleep(5)

# # #             # Find the selected product details
# # #             selected_product = next(p for p in products if f"{p['product_name']} (Brand: {p.get('brands', 'Unknown')})" == selected_product_name)

# # #             # Display selected product name
# # #             st.write(f"### Selected Product: {selected_product['product_name']} (Brand: {selected_product.get('brands', 'Unknown')})")

# # #             if selected_product:
# # #                 summary = generate_summary(selected_product, tone)
# # #                 st.write(f"### Summary:")
# # #                 st.write(summary)

# # # if __name__ == "__main__":
# # #     main()


# # import requests
# # import google.generativeai as genai
# # import streamlit as st

# # # Configure Gemini API (Use your actual API key)
# # genai.configure(api_key='AIzaSyD5yLv8zkGNC7YbxxODLqlMJJKTv8VWdQw')

# # # Function to get data from OpenFoodFacts API
# # def get_data(product_name):
# #     url = "https://world.openfoodfacts.org/cgi/search.pl"
# #     params = {
# #         'search_terms': product_name,
# #         'search_simple': 1,
# #         'json': 1,
# #     }
# #     response = requests.get(url, params=params)
# #     data = response.json()
# #     if 'products' not in data or len(data['products']) == 0:
# #         return []  # Return empty if no products found

# #     # Filter products with names and return top 5
# #     data['products'] = [p for p in data['products'] if 'product_name' in p]
# #     return data['products'][:5]

# # # Function to generate product analysis using Gemini
# # def generate_summary(product, tone):
# #     name = product.get('product_name', 'Not mentioned')
# #     brand = product.get('brands', 'Not mentioned')
# #     nutriscore_grade = product.get('nutriscore_grade', 'Not mentioned')
# #     eco_score = product.get('ecoscore_grade', 'Not mentioned')
# #     packaging = product.get('packaging', 'Not mentioned')
# #     ingredients = product.get('ingredients_text', 'Not mentioned')
# #     nutrients = product.get('nutriments', 'Not mentioned')
# #     nova = product.get('nova_groups_tags', 'Not mentioned')

# #     # Generate prompt based on tone
# #     prompt = f"""
# #     You are an AI assistant analyzing consumer products. Here are the details:
# #     - Name: {name}
# #     - Brand: {brand}
# #     - EcoScore: {eco_score}
# #     - NutriScore: {nutriscore_grade}
# #     - NovaScore: {nova}
# #     - Ingredients: {ingredients}
# #     - Nutrients: {nutrients}
# #     - Packaging: {packaging}

# #     Please provide a {tone} analysis including:
# #     1. Positive aspects of the product.
# #     2. Negative aspects of the product.
# #     3. Health impact.
# #     4. Environmental impact.
# #     """

# #     model = genai.GenerativeModel(model_name="gemini-1.5-flash")
# #     response = model.generate_content(prompt)
# #     return response.text

# # # Streamlit interface
# # def main():
# #     st.title("ConsumeNice")
# #     st.write("Get product details and summaries using OpenFoodFacts and Gemini AI.")

# #     product_input = st.text_input("Product Name", placeholder="Enter the product name...")
# #     tone = st.radio("Summary Tone", options=["simple", "deeper"], index=0)

# #     if st.button("Search"):
# #         products = get_data(product_input)
# #         if not products:
# #             st.error("No products found for the given name.")
# #         else:
# #             product_names = [f"{p['product_name']} (Brand: {p.get('brands', 'Unknown')})" for p in products]
# #             selected_product_name = st.radio("Select a Product", product_names, key='product_selection')

# #             # Find the selected product details
# #             selected_product = next(p for p in products if f"{p['product_name']} (Brand: {p.get('brands', 'Unknown')})" == selected_product_name)

# #             # Display selected product name
# #             st.write(f"### Selected Product: {selected_product['product_name']} (Brand: {selected_product.get('brands', 'Unknown')})")

# #             if selected_product:
# #                 # Use session state to retain summary across selections
# #                 if 'summary' not in st.session_state:
# #                     st.session_state.summary = None

# #                 summary = generate_summary(selected_product, tone)
# #                 st.session_state.summary = summary

# #                 st.write(f"### Summary:")
# #                 st.write(st.session_state.summary)

# # if __name__ == "__main__":
# #     main()
# # import requests
# # import google.generativeai as genai
# # import streamlit as st

# # # Configure Gemini API (Use your actual API key)
# # genai.configure(api_key='AIzaSyD5yLv8zkGNC7YbxxODLqlMJJKTv8VWdQw')

# # # Function to get data from OpenFoodFacts API
# # def get_data(product_name):
# #     url = "https://world.openfoodfacts.org/cgi/search.pl"
# #     params = {
# #         'search_terms': product_name,
# #         'search_simple': 1,
# #         'json': 1,
# #     }
# #     response = requests.get(url, params=params)
# #     data = response.json()
# #     if 'products' not in data or len(data['products']) == 0:
# #         return []  # Return empty if no products found

# #     # Filter products with names and return top 5
# #     data['products'] = [p for p in data['products'] if 'product_name' in p]
# #     return data['products'][:5]

# # # Function to generate product analysis using Gemini
# # def generate_summary(product, tone):
# #     name = product.get('product_name', 'Not mentioned')
# #     brand = product.get('brands', 'Not mentioned')
# #     nutriscore_grade = product.get('nutriscore_grade', 'Not mentioned')
# #     eco_score = product.get('ecoscore_grade', 'Not mentioned')
# #     packaging = product.get('packaging', 'Not mentioned')
# #     ingredients = product.get('ingredients_text', 'Not mentioned')
# #     nutrients = product.get('nutriments', 'Not mentioned')
# #     nova = product.get('nova_groups_tags', 'Not mentioned')

# #     # Generate prompt based on tone
# #     prompt = f"""
# #     You are an AI assistant analyzing consumer products. Here are the details:
# #     - Name: {name}
# #     - Brand: {brand}
# #     - EcoScore: {eco_score}
# #     - NutriScore: {nutriscore_grade}
# #     - NovaScore: {nova}
# #     - Ingredients: {ingredients}
# #     - Nutrients: {nutrients}
# #     - Packaging: {packaging}

# #     Please provide a {tone} analysis including:
# #     1. Positive aspects of the product.
# #     2. Negative aspects of the product.
# #     3. Health impact.
# #     4. Environmental impact.
# #     """

# #     model = genai.GenerativeModel(model_name="gemini-1.5-flash")
# #     response = model.generate_content(prompt)
# #     return response.text

# # # Streamlit interface
# # def main():
# #     st.title("ConsumeNice")
# #     st.write("Get product details and summaries using OpenFoodFacts and Gemini AI.")

# #     product_input = st.text_input("Product Name", placeholder="Enter the product name...")
# #     tone = st.radio("Summary Tone", options=["simple", "deeper"], index=0)

# #     if st.button("Search"):
# #         products = get_data(product_input)
# #         if not products:
# #             st.error("No products found for the given name.")
# #         else:
# #             product_names = [f"{p['product_name']} (Brand: {p.get('brands', 'Unknown')})" for p in products]
# #             selected_product_name = st.radio("Select a Product", product_names, key='product_selection')

# #             # Find the selected product details
# #             selected_product = next(p for p in products if f"{p['product_name']} (Brand: {p.get('brands', 'Unknown')})" == selected_product_name)

# #             # Display selected product name
# #             st.write(f"### Selected Product: {selected_product['product_name']} (Brand: {selected_product.get('brands', 'Unknown')})")

# #             if selected_product:
# #                 # Use session state to retain summary across selections
# #                 if 'summary' not in st.session_state:
# #                     st.session_state.summary = None

# #                 summary = generate_summary(selected_product, tone)
# #                 st.session_state.summary = summary

# #                 st.write(f"### Summary:")
# #                 st.write(st.session_state.summary)

# # if _name_ == "_main_":
# #     main()

# # import requests
# # import google.generativeai as genai
# # import streamlit as st

# # # Configure Gemini API (Use your actual API key)
# # genai.configure(api_key='AIzaSyD5yLv8zkGNC7YbxxODLqlMJJKTv8VWdQw')

# # # Function to get data from OpenFoodFacts API
# # def get_data(product_name):
# #     url = "https://world.openfoodfacts.org/cgi/search.pl"
# #     params = {
# #         'search_terms': product_name,
# #         'search_simple': 1,
# #         'json': 1,
# #     }
# #     response = requests.get(url, params=params)
# #     data = response.json()
# #     if 'products' not in data or len(data['products']) == 0:
# #         return []  # Return empty if no products found

# #     # Filter products with names and return top 5
# #     data['products'] = [p for p in data['products'] if 'product_name' in p]
# #     return data['products'][:5]

# # # Function to generate product analysis using Gemini
# # def generate_summary(product, tone):
# #     name = product.get('product_name', 'Not mentioned')
# #     brand = product.get('brands', 'Not mentioned')
# #     nutriscore_grade = product.get('nutriscore_grade', 'Not mentioned')
# #     eco_score = product.get('ecoscore_grade', 'Not mentioned')
# #     packaging = product.get('packaging', 'Not mentioned')
# #     ingredients = product.get('ingredients_text', 'Not mentioned')
# #     nutrients = product.get('nutriments', 'Not mentioned')
# #     nova = product.get('nova_groups_tags', 'Not mentioned')

# #     # Generate prompt based on tone
# #     prompt = f"""
# #     You are an AI assistant analyzing consumer products. Here are the details:
# #     - Name: {name}
# #     - Brand: {brand}
# #     - EcoScore: {eco_score}
# #     - NutriScore: {nutriscore_grade}
# #     - NovaScore: {nova}
# #     - Ingredients: {ingredients}
# #     - Nutrients: {nutrients}
# #     - Packaging: {packaging}

# #     Please provide a {tone} analysis including:
# #     1. Positive aspects of the product.
# #     2. Negative aspects of the product.
# #     3. Health impact.
# #     4. Environmental impact.
# #     """

# #     model = genai.GenerativeModel(model_name="gemini-1.5-flash")
# #     response = model.generate_content(prompt)
# #     return response.text

# # # Streamlit interface
# # def main():
# #     # Page setup and header
# #     st.set_page_config(page_title="ConsumeNice", page_icon="🍽️", layout="centered")
# #     st.title("🍽️ ConsumeNice - Product Analysis with AI")
# #     st.write("Welcome to *ConsumeNice*, Know What You Eat")

# #     st.sidebar.title("Developed by:")
# #     st.sidebar.markdown("*Srish*")
# #     st.sidebar.markdown("[LinkedIn](https://www.linkedin.com/in/srishrachamalla/)")
# #     st.sidebar.markdown("*Sai Teja*")
# #     st.sidebar.markdown("[LinkedIn](https://www.linkedin.com/in/saiteja-pallerla-668734225/)")
    
# #     st.sidebar.title("Additional Info")
# #     st.sidebar.markdown("This app allows you to search for a product and get an AI-generated analysis.")

# #     # Input fields
# #     product_input = st.text_input("Enter Product Name", placeholder="Type product name to search...")
# #     tone = st.radio("Select Summary Tone", options=["Simple", "Deeper"], index=0)

# #     if st.button("Search"):
# #         with st.spinner("Fetching product data..."):
# #             products = get_data(product_input)
# #         if not products:
# #             st.error("No products found for the given name.")
# #         else:
# #             product_names = [f"{p['product_name']} (Brand: {p.get('brands', 'Unknown')})" for p in products]
# #             selected_product_name = st.radio("Select a Product", product_names, key='product_selection')

# #             # Find the selected product details
# #             selected_product = next(p for p in products if f"{p['product_name']} (Brand: {p.get('brands', 'Unknown')})" == selected_product_name)

# #             # Display selected product name
# #             st.write(f"### Selected Product: *{selected_product['product_name']}* (Brand: {selected_product.get('brands', 'Unknown')})")

# #             if selected_product:
# #                 # Use session state to retain summary across selections
# #                 if 'summary' not in st.session_state:
# #                     st.session_state.summary = None

# #                 with st.spinner("Generating AI analysis..."):
# #                     summary = generate_summary(selected_product, tone)
# #                 st.session_state.summary = summary

# #                 # Display summary
# #                 st.write("### Summary:")
# #                 st.success(st.session_state.summary)

# #     # Footer section
# #     st.markdown("---")
# #     st.write("### About the Hackathon Project")
# #     st.info("This project was developed as part of a hackathon challenge to showcase AI Skills. Built using OpenFoodFacts and Google's Gemini.")

# # if _name_ == "_main_":
# #     main()

# import requests
# import google.generativeai as genai
# import streamlit as st
# from PIL import Image

# # Configure Gemini API (Use your actual API key)
# genai.configure(api_key='AIzaSyD5yLv8zkGNC7YbxxODLqlMJJKTv8VWdQw')

# # Function to get data from OpenFoodFacts API
# def get_data(product_name):
#     url = "https://world.openfoodfacts.org/cgi/search.pl"
#     params = {
#         'search_terms': product_name,
#         'search_simple': 1,
#         'json': 1,
#     }
#     response = requests.get(url, params=params)
#     data = response.json()
#     if 'products' not in data or len(data['products']) == 0:
#         return []  # Return empty if no products found

#     # Filter products with names and return top 5
#     data['products'] = [p for p in data['products'] if 'product_name' in p]
#     return data['products'][:5]

# # Function to generate product analysis using Gemini
# def generate_summary(product, tone):
#     name = product.get('product_name', 'Not mentioned')
#     brand = product.get('brands', 'Not mentioned')
#     nutriscore_grade = product.get('nutriscore_grade', 'Not mentioned')
#     eco_score = product.get('ecoscore_grade', 'Not mentioned')
#     packaging = product.get('packaging', 'Not mentioned')
#     ingredients = product.get('ingredients_text', 'Not mentioned')
#     nutrients = product.get('nutriments', 'Not mentioned')
#     nova = product.get('nova_groups_tags', 'Not mentioned')

#     # Generate prompt based on tone
#     prompt = f"""
#     You are an AI assistant analyzing consumer products. Here are the details:
#     - Name: {name}
#     - Brand: {brand}
#     - EcoScore: {eco_score}
#     - NutriScore: {nutriscore_grade}
#     - NovaScore: {nova}
#     - Ingredients: {ingredients}
#     - Nutrients: {nutrients}
#     - Packaging: {packaging}

#     Please provide a {tone} analysis including:
#     1. Positive aspects of the product.
#     2. Negative aspects of the product.
#     3. Health impact.
#     4. Environmental impact.
#     """

#     model = genai.GenerativeModel(model_name="gemini-1.5-flash")
#     response = model.generate_content(prompt)
#     return response.text

# # Streamlit interface
# def main():
#     # Page setup and header with background image
#     st.set_page_config(page_title="ConsumeNice", page_icon="🍽️", layout="centered")

#     # Custom CSS for better aesthetics
#     # st.markdown(
#     #     """
#     #     <style>
#     #     .main {background-color: #f0f2f6;}
#     #     .reportview-container .main .block-container {
#     #         padding-top: 2rem;
#     #         padding-right: 3rem;
#     #         padding-left: 3rem;
#     #     }
#     #     .css-1d391kg {color: #ff4b4b !important;}
#     #     .css-145kmo2 {color: #00b4d8 !important;}
#     #     h1 {color: #1f3b4d !important;}
#     #     .stButton>button {background-color: #f63366; color: white;}
#     #     .stTextInput>div>input {padding: 12px; border-radius: 6px; border: 1px solid #00b4d8;}
#     #     .stRadio>div>label {color: #1f3b4d !important;}
#     #     </style>
#     #     """, 
#     #     unsafe_allow_html=True
#     # )
#     st.markdown(
#         """
#         <style>
#         .main {background-color: #000000;}
#         .reportview-container .main .block-container {
#             padding-top: 2rem;
#             padding-right: 2.5rem;
#             padding-left: 2.5rem;
#         }
#         h1, h2, h3, h4, h5 {color: #ffffff;}
#         .stButton>button {
#             background-color: #6c757d; 
#             color: white;
#             border-radius: 8px;
#         }
#         .stButton>button:hover {
#             background-color: #5a6268;
#         }
#         .stTextInput>div>input {
#             padding: 10px; 
#             border-radius: 6px; 
#             border: 1px solid #ced4da;
#             background-color: #f8f9fa;
#         }
#         .stRadio>div>label {color: #495057 !important;}
#         .css-1d391kg {color: #495057 !important;}
#         .css-145kmo2 {color: #495057 !important;}
#         </style>
#         """, 
#         unsafe_allow_html=True
#     )


#     # App logo (assuming you have an image named 'logo.png' in the same directory)
#     st.image(Image.open(r'C:\projects\google hack\googlehack2\TEST_wise\static\images\logo.png'), width=120, caption="ConsumeNice - Know What You Consume", )
#     # Custom HTML for displaying the image and caption side by side
# #     image = Image.open(r'C:\Projects\google hack\test\static\images\logo.png')
# #     st.markdown(
# #     f"""
# #     <div style="display: flex; align-items: center;">
# #         <img src="data:image/png;base64,{st.image(image, use_column_width=False)}" style="width: 10px;">
# #         <p style="margin-left: 20px; font-size: 18px;">ConsumeNice - Know What You Consume</p>
# #     </div>
# #     """,
# #     unsafe_allow_html=True
# # )

#     # st.title("🍽️ ConsumeNice - Analyze Products with AI")
#     st.markdown(
#     """
#     <h1 style='text-align: center; color: #fffff;'>🍽️ ConsumeNice - Analyze Products with AI</h1>
#     """, 
#     unsafe_allow_html=True
# )
#     st.write("Welcome to *ConsumeNice*, where you can search for products and get an AI-generated analysis based on their nutritional, environmental, and packaging details. Built with OpenFoodFacts and Gemini AI.")
    
#     # Sidebar for developer profiles and hackathon info
#     # st.sidebar.title("Developers - 👨‍💻")
# #     st.sidebar.markdown(
# #     """
# #     <h1 style='color: #0072B2;'>Developers - 👨‍💻</h1>
# #     """, 
# #     unsafe_allow_html=True
# # )
# #     st.sidebar.markdown("[LinkedIn - Srish](https://www.linkedin.com/in/srish-linkedin-url)")
    
# #     st.sidebar.markdown("[LinkedIn - Sai Teja](https://www.linkedin.com/in/sai-teja-linkedin-url)")

# #     # st.sidebar.title("Hackathon Project")
# #     st.sidebar.markdown(
# #     """
# #     <h1 style='color: #0072B2;'>Hackathon Project</h1>
# #     """, 
# #     unsafe_allow_html=True
# # )
# #     st.sidebar.markdown("This project showcases AI integration to analyze consumer products.")
#     # Sidebar content with custom formatting
#     st.sidebar.markdown(
#         """
#         <h1 style='color: #0072B2;'>🚀 Hackathon Project</h1>
#         """, 
#         unsafe_allow_html=True
#     )

#     st.sidebar.markdown("Welcome to the *ConsumeNice* project, developed for the hackathon to showcase AI integration in product analysis.")

#     # Add some icons/emojis to make it look more engaging
#     st.sidebar.markdown("### 🔧 Project Features")
#     st.sidebar.markdown("- Analyze product details using *OpenFoodFacts* API.")
#     st.sidebar.markdown("- AI-generated analysis using *Google Gemini AI*.")
#     st.sidebar.markdown("- Environment, packaging, and health analysis.")

#     # Developer details with LinkedIn links
#     st.sidebar.markdown("### 👨‍💻 Developers")
#     st.sidebar.markdown("[*Srish*](https://www.linkedin.com/in/srishrachamalla/) - AI/ML Developer")
#     st.sidebar.markdown("[*Sai Teja*](https://www.linkedin.com/in/saiteja-pallerla-668734225/) - Data Analyst")

#     # Add expander sections for additional content
#     with st.sidebar.expander("ℹ️ About ConsumeNice"):
#         st.write("*ConsumeNice* is designed to give consumers more insights into the products they consume, analyzing factors like health impact, environmental footprint, and packaging.")

#     with st.sidebar.expander("📚 Useful Resources"):
#         st.write("[Google Gemini AI Documentation](https://ai.google.dev/)")
#         st.write("[Streamlit Documentation](https://docs.streamlit.io/)")

#     # Add progress indicator for hackathon phases or development stages
#     st.sidebar.markdown("### ⏳ Hackathon Progress")
#     st.sidebar.progress(0.99)  # Set progress level (0 to 1)

#     # Sidebar footer with final notes
#     st.sidebar.markdown("---")
#     st.sidebar.markdown(
#         """
#         <div style="text-align: center; font-size: 0.85em;">
#             Developed by Srish & Sai Teja • Powered by Google Gemini AI
#         </div>
#         """, unsafe_allow_html=True
#     )


#     # User input fields with improved placeholders and hints
#     product_input = st.text_input("Enter Product Name", placeholder="e.g., Coca-Cola, Oreo, Dove Soap")
#     tone = st.radio("Choose Analysis Depth", options=["Simple", "In-depth"], index=0)

#     if st.button("Search"):
#         with st.spinner("Searching for products..."):
#             products = get_data(product_input)
        
#         if not products:
#             st.error("No products found for the given name.")
#         else:
#             product_names = [f"{p['product_name']} (Brand: {p.get('brands', 'Unknown')})" for p in products]
#             selected_product_name = st.radio("Select a Product", product_names, key='product_selection')

#             selected_product = next(p for p in products if f"{p['product_name']} (Brand: {p.get('brands', 'Unknown')})" == selected_product_name)

#             st.write(f"### Product Selected: *{selected_product['product_name']}* (Brand: {selected_product.get('brands', 'Unknown')})")

#             if selected_product:
#                 if 'summary' not in st.session_state:
#                     st.session_state.summary = None

#                 with st.spinner("Generating AI-powered analysis..."):
#                     summary = generate_summary(selected_product, tone.lower())
#                 st.session_state.summary = summary

#                 st.write("### Product Analysis Summary:")
#                 st.success(st.session_state.summary)

#     # Footer with hackathon and design details
#     st.markdown("---")
#     st.markdown("""
#         <div style="text-align: center; font-size: 0.9em;">
#         <p><i>ConsumeNice</i> was developed for a hackathon using <b>Streamlit</b> to showcase AI integration with real-world data sources like OpenFoodFacts.</p>
#         <p>Developed by Srish & Sai Teja • Powered by Google Gemini AI</p>
#         </div>
#         """, unsafe_allow_html=True)

# if __name__ == "__main__":
#     main()
# import requests
# import google.generativeai as genai
# import streamlit as st
# from PIL import Image

# # Configure Gemini API (Use your actual API key)
# genai.configure(api_key='AIzaSyD5yLv8zkGNC7YbxxODLqlMJJKTv8VWdQw')

# # Function to get data from OpenFoodFacts API
# def get_data(product_name):
#     url = "https://world.openfoodfacts.org/cgi/search.pl"
#     params = {
#         'search_terms': product_name,
#         'search_simple': 1,
#         'json': 1,
#     }
#     response = requests.get(url, params=params)
#     data = response.json()
#     if 'products' not in data or len(data['products']) == 0:
#         return []  # Return empty if no products found

#     # Filter products with names and return top 5
#     data['products'] = [p for p in data['products'] if 'product_name' in p]
#     return data['products'][:5]

# # Function to generate product analysis using Gemini
# def generate_summary(product, tone):
#     name = product.get('product_name', 'Not mentioned')
#     brand = product.get('brands', 'Not mentioned')
#     nutriscore_grade = product.get('nutriscore_grade', 'Not mentioned')
#     eco_score = product.get('ecoscore_grade', 'Not mentioned')
#     packaging = product.get('packaging', 'Not mentioned')
#     ingredients = product.get('ingredients_text', 'Not mentioned')
#     nutrients = product.get('nutriments', 'Not mentioned')
#     nova = product.get('nova_groups_tags', 'Not mentioned')

#     # Generate prompt based on tone
#     prompt = f"""
#     You are an AI assistant analyzing consumer products. Here are the details:
#     - Name: {name}
#     - Brand: {brand}
#     - EcoScore: {eco_score}
#     - NutriScore: {nutriscore_grade}
#     - NovaScore: {nova}
#     - Ingredients: {ingredients}
#     - Nutrients: {nutrients}
#     - Packaging: {packaging}

#     Please provide a {tone} analysis including:
#     1. Positive aspects of the product.
#     2. Negative aspects of the product.
#     3. Health impact.
#     4. Environmental impact.
#     """

#     model = genai.GenerativeModel(model_name="gemini-1.5-flash")
#     response = model.generate_content(prompt)
#     return response.text

# # Streamlit interface
# def main():
#     # Page setup and header with background image
#     st.set_page_config(page_title="ConsumeNice", page_icon="🍽️", layout="centered")

#     # Custom CSS for better aesthetics
#     st.markdown(
#         """
#         <style>
#         .main {background-color: #000000;}
#         .reportview-container .main .block-container {
#             padding-top: 2rem;
#             padding-right: 2.5rem;
#             padding-left: 2.5rem;
#         }
#         h1, h2, h3, h4, h5 {color: #ffffff;}
#         .stButton>button {
#             background-color: #6c757d; 
#             color: white;
#             border-radius: 8px;
#         }
#         .stButton>button:hover {
#             background-color: #5a6268;
#         }
#         .stTextInput>div>input {
#             padding: 10px; 
#             border-radius: 6px; 
#             border: 1px solid #ced4da;
#             background-color: #f8f9fa;
#         }
#         .stRadio>div>label {color: #495057 !important;}
#         .css-1d391kg {color: #495057 !important;}
#         .css-145kmo2 {color: #495057 !important;}
#         </style>
#         """, 
#         unsafe_allow_html=True
#     )

#     # App logo and header side by side
#     col1, col2 = st.columns([1, 3])  # Adjust proportions as needed
#     with col1:
#         st.image(Image.open(r'C:\projects\google hack\googlehack2\TEST_wise\static\images\logo.png'), width=120, caption="ConsumeNice - Know What You Consume")
#     with col2:
#         st.markdown(
#             "<h1 style='text-align: left; color: #ffffff;'>🍽️ ConsumeNice - Analyze Products with AI</h1>", 
#             unsafe_allow_html=True
#         )

#     st.write("Welcome to *ConsumeNice*, where you can search for products and get an AI-generated analysis based on their nutritional, environmental, and packaging details. Built with OpenFoodFacts and Gemini AI.")
    
#     # Sidebar for developer profiles and hackathon info
#     st.sidebar.markdown(
#         """
#         <h1 style='color: #0072B2;'>🚀 Hackathon Project</h1>
#         """, 
#         unsafe_allow_html=True
#     )
#     st.sidebar.markdown("Welcome to the *ConsumeNice* project, developed for the hackathon to showcase AI integration in product analysis.")

#     # Add some icons/emojis to make it look more engaging
#     st.sidebar.markdown("### 🔧 Project Features")
#     st.sidebar.markdown("- Analyze product details using *OpenFoodFacts* API.")
#     st.sidebar.markdown("- AI-generated analysis using *Google Gemini AI*.")
#     st.sidebar.markdown("- Environment, packaging, and health analysis.")

#     # Developer details with LinkedIn links
#     st.sidebar.markdown("### 👨‍💻 Developers")
#     st.sidebar.markdown("[*Srish*](https://www.linkedin.com/in/srishrachamalla/) - AI/ML Developer")
#     st.sidebar.markdown("[*Sai Teja*](https://www.linkedin.com/in/saiteja-pallerla-668734225/) - Data Analyst")

#     # Add expander sections for additional content
#     with st.sidebar.expander("ℹ️ About ConsumeNice"):
#         st.write("*ConsumeNice* is designed to give consumers more insights into the products they consume, analyzing factors like health impact, environmental footprint, and packaging.")

#     with st.sidebar.expander("📚 Useful Resources"):
#         st.write("[Google Gemini AI Documentation](https://ai.google.dev/gemini-api/docs)")
#         st.write("[Streamlit Documentation](https://docs.streamlit.io/)")

#     # Add progress indicator for hackathon phases or development stages
#     st.sidebar.markdown("### ⏳ Hackathon Progress")
#     st.sidebar.progress(0.99)  # Set progress level (0 to 1)

#     # Sidebar footer with final notes
#     st.sidebar.markdown("---")
#     st.sidebar.markdown(
#         """
#         <div style="text-align: center; font-size: 0.85em;">
#             Developed by Srish & Sai Teja • Powered by Google Gemini AI
#         </div>
#         """, unsafe_allow_html=True
#     )

#     # User input fields with improved placeholders and hints
#     product_input = st.text_input("Enter Product Name", placeholder="e.g., Coca-Cola, Oreo, Dove Soap")
#     tone = st.radio("Choose Analysis Depth", options=["Simple", "In-depth"], index=0)

#     if st.button("Search"):
#         with st.spinner("Searching for products..."):
#             products = get_data(product_input)
        
#         if not products:
#             st.error("No products found for the given name.")
#         else:
#             product_names = [f"{p['product_name']} (Brand: {p.get('brands', 'Unknown')})" for p in products]
#             selected_product_name = st.radio("Select a Product", product_names, key='product_selection')

#             selected_product = next(p for p in products if f"{p['product_name']} (Brand: {p.get('brands', 'Unknown')})" == selected_product_name)

#             st.write(f"### Product Selected: *{selected_product['product_name']}* (Brand: {selected_product.get('brands', 'Unknown')})")

#             if selected_product:
#                 if 'summary' not in st.session_state:
#                     st.session_state.summary = None

#                 with st.spinner("Generating AI-powered analysis..."):
#                     summary = generate_summary(selected_product, tone.lower())
#                 st.session_state.summary = summary

#                 st.write("### Product Analysis Summary:")
#                 st.success(st.session_state.summary)

#     # Footer with hackathon and design details
#     st.markdown("---")
#     st.markdown("""
#         <div style="text-align: center; font-size: 0.9em;">
#         <p><i>ConsumeNice</i> was developed for a hackathon using <b>Streamlit</b> to showcase AI integration with real-world data sources like OpenFoodFacts.</p>
#         <p>Developed by Srish & Sai Teja • Powered by Google Gemini AI</p>
#         </div>
#         """, unsafe_allow_html=True)

# if __name__ == "__main__":
#     main()
import requests
import google.generativeai as genai
import streamlit as st
from PIL import Image

# Configure Gemini API (Use your actual API key)
genai.configure(api_key='AIzaSyD5yLv8zkGNC7YbxxODLqlMJJKTv8VWdQw')

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
    return data['products'][:5]

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
    st.set_page_config(page_title="ConsumeNice", page_icon="🍽️", layout="centered")

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
        st.image(Image.open(r'C:\projects\google hack\googlehack2\TEST_wise\static\images\logo.png'), width=120, caption="ConsumeNice - Know What You Consume")
    with col2:
        st.markdown(
            "<h1 style='text-align: left; color: #ffffff;'>🍽️ ConsumeNice - Analyze Products with AI</h1>", 
            unsafe_allow_html=True
        )

    st.write("Welcome to *ConsumeNice*, where you can search for products and get an AI-generated analysis based on their nutritional, environmental, and packaging details. Built with OpenFoodFacts and Gemini AI.")
    
    # Sidebar for developer profiles and hackathon info
    st.sidebar.markdown(
        """
        <h1 style='color: #0072B2;'>🚀 Hackathon Project</h1>
        """, 
        unsafe_allow_html=True
    )
    st.sidebar.markdown("Welcome to the *ConsumeNice* project, developed for the hackathon to showcase AI integration in product analysis.")

    # Add some icons/emojis to make it look more engaging
    st.sidebar.markdown("### 🔧 Project Features")
    st.sidebar.markdown("- Analyze product details using *OpenFoodFacts* API.")
    st.sidebar.markdown("- AI-generated analysis using *Google Gemini AI*.")
    st.sidebar.markdown("- Environment, packaging, and health analysis.")

    # Developer details with LinkedIn links
    st.sidebar.markdown("### 👨‍💻 Developers")
    st.sidebar.markdown("[*Srish*](https://www.linkedin.com/in/srishrachamalla/) - AI/ML Developer")
    st.sidebar.markdown("[*Sai Teja*](https://www.linkedin.com/in/saiteja-pallerla-668734225/) - Data Analyst")

    # Add expander sections for additional content
    with st.sidebar.expander("ℹ️ About ConsumeNice"):
        st.write("*ConsumeNice* is designed to give consumers more insights into the products they consume, analyzing factors like health impact, environmental footprint, and packaging.")

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

    if st.button("Search"):
        with st.spinner("Searching for products..."):
            products = get_data(product_input)
        
        if not products:
            st.error("No products found for the given name.")
        else:
            # Display products with images and URLs
            st.write("### Search Results:")
            for product in products:
                product_name = product.get('product_name', 'Unknown Product')
                product_brand = product.get('brands', 'Unknown Brand')
                product_image = product.get('image_url', None)
                product_url = product.get('url', '#')

                # Display product image, name, and URL
                col1, col2 = st.columns([1, 3])  # Adjust proportions as needed
                with col1:
                    if product_image:
                        st.image(product_image, width=100)
                with col2:
                    st.markdown(f"**{product_name}** (Brand: {product_brand})")
                    st.markdown(f"[View Product]({product_url})", unsafe_allow_html=True)

            selected_product_name = st.radio("Select a Product", 
                                              [f"{p['product_name']} (Brand: {p.get('brands', 'Unknown')})" for p in products],
                                              key='product_selection')

            selected_product = next(p for p in products if f"{p['product_name']} (Brand: {p.get('brands', 'Unknown')})" == selected_product_name)

            st.write(f"### Product Selected: *{selected_product['product_name']}* (Brand: {selected_product.get('brands', 'Unknown')})")

            if selected_product:
                if 'summary' not in st.session_state:
                    st.session_state.summary = None

                with st.spinner("Generating AI-powered analysis..."):
                    summary = generate_summary(selected_product, tone.lower())
                st.session_state.summary = summary

                st.write("### Product Analysis Summary:")
                st.success(st.session_state.summary)

    # Footer with hackathon and design details
    st.markdown("---")
    st.markdown("""<div style="text-align: center; font-size: 0.9em;">
        <p><i>ConsumeNice</i> was developed for a hackathon using <b>Streamlit</b> to showcase AI integration with real-world data sources like OpenFoodFacts.</p>
        <p>Developed by Srish & Sai Teja • Powered by Google Gemini AI</p>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

