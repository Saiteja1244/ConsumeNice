
import requests
import google.generativeai as genai

class OpenFoodFacts:
    # Function to get data from OpenFoodFacts API
    def get_data(self,product_name):
        
        url = "https://world.openfoodfacts.org/cgi/search.pl"
        params = {
            'search_terms': product_name,
            'search_simple': 1,
            'json': 1,
            'tagtype_0': 'countries',   # Filter by country
            'tag_contains_0': 'contains',
            'tag_0': 'India',
        }
        response = requests.get(url, params=params)
        data = response.json()
        return data['products'][:5]  # Return top 5 results

    # Function to extract specific info from product
    def product_info_extraction(self,product):
        name = product.get('product_name', 'Not mentioned')
        brand = product.get('brands', 'Not mentioned')
        image_url = product.get('image_url', 'Not mentioned')
        web_url = product.get('url', 'Not mentioned')
        return {"name": name, "brand": brand, "image_url": image_url, "web_url": web_url}

    # Function to generate LLM prompt
    def LLM(self,product, tone):
        name = product.get('product_name', 'Not mentioned')
        brand = product.get('brands', 'Not mentioned')
        nutriscore_grade = product.get('nutriscore_grade', 'Not mentioned')
        eco_score = product.get('ecoscore_grade', 'Not mentioned')
        packaging = product.get('packaging', 'Not mentioned')
        ingredients = product.get('ingredients_text', 'Not mentioned')
        nutrients = product.get('nutrients_data', 'Not mentioned')
        image_url = product.get('image_url', 'Not mentioned')
        web_url = product.get('url', 'Not mentioned')
        barcode = product.get('_id')
        vitamins = product.get('vitamins_tags', 'Not mentioned')
        keywords = product.get('_keywords', 'Not mentioned')
        nova = product.get('nova_groups_tags', 'Not mentioned')


        # Generate prompt based on tone
        if tone == 'simple':
            prompt = f"""
            The product name is {name}, brand is {brand}, and its eco-score is {eco_score}, nutriscore grade is {nutriscore_grade}.
            Provide a simple analysis including:
            1. Positive aspects.
            2. Negative aspects.
            3. Health impact.
            4. Environmental impact.
            """
        else:
            # prompt = f"""
            # You are an AI assistant analyzing consumer products.Here are the details
            # - Name: {name}
            # - Brand: {brand}
            # - EcoScore: {eco_score}
            # - NutriScore: {nutriscore_grade}
            # - NovaScore : {nova}
            # - Ingredients: {ingredients}
            # - NutriScore: {nutrients}
            # - Packaging: {packaging}
            # - Nutrients: {nutrients}
            # - Vitamins: {vitamins}
            # - Keywords: {keywords}
            # if the data is unavailable dont say it as unavailable and never mention it is form open food facts
            # show nutriscore, novascore and ecoscore and display it in the start and give the description of the scores as i said these data is comming from the open food facts api so give accordingly
            # Your task is to provide an in-depth analysis of the product, focusing on:
            # 1. Health impact: Explain how the ingredients, nutrients, and vitamins might affect human health.
            # 2. Environmental impact: Assess the sustainability and environmental friendliness of the product, particularly its packaging.

            # The data comes from the Open Food Facts dataset. Please ensure your response is informative and clear, helping users make conscious decisions about their health and the environment.
            # ex:
            # and if **NovaScore:** **['en:4-ultra-processed-food-and-drink-products']** 
            # make it **NovaScore:** **4-ultra-processed**
            # """
            prompt = f"""
    You are an AI assistant analyzing consumer products. Here are the details:
    - Name: {name}
    - Brand: {brand}
    - EcoScore: {eco_score if eco_score else 'This product’s EcoScore is currently not specified, but its sustainability may vary based on its packaging and ingredients.'}
    - NutriScore: {nutriscore_grade if nutriscore_grade else 'The NutriScore for this product is not available at the moment, but it is crucial for evaluating health impacts.'}
    - NovaScore: {nova if nova else 'While the NovaScore isn’t specified, it’s essential to consider how processed a product is when evaluating its healthiness.'}
    - Ingredients: {ingredients if ingredients else 'This product contains a blend of ingredients typical for carbonated beverages.'}
    - Nutrients: {nutrients if nutrients else 'Nutritional information is valuable for understanding the health implications of this beverage.'}
    - Packaging: {packaging if packaging else 'The packaging can significantly influence the product’s environmental footprint.'}
    - Vitamins: {vitamins if vitamins else 'Vitamins play an essential role in health, and their presence can affect overall wellbeing.'}
    - Keywords: {keywords if keywords else 'Relevant keywords can highlight important features of the product.'}

    Please summarize the NutriScore, NovaScore, and EcoScore at the beginning and provide a description of each score as mentioned above. Your task is to provide an in-depth analysis of the product, focusing on:
    1. Health impact: Explain how the ingredients, nutrients, and vitamins might affect human health.
    2. Environmental impact: Assess the sustainability and environmental friendliness of the product, particularly its packaging.

    Ensure your response is informative and clear, helping users make conscious decisions about their health and the environment. Do not explicitly mention if any data is unknown or unavailable; instead, provide context or general information when specific data points are missing.
    """


        genai.configure(api_key='AIzaSyD5yLv8zkGNC7YbxxODLqlMJJKTv8VWdQw')
        model = genai.GenerativeModel(model_name="gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text


    def interface(self,product_name):
        # Step 1: Fetch product data
        products = self.get_data(product_name)
        #   print(products)
        # Step 2: Extract product info and show in table
        extracted_data = [self.product_info_extraction(p) for p in products]
        #   print(extracted_data)

        # Create Gradio components
        for p in extracted_data:
            print("name is " + p['name'])
            print("brand is " + p['brand'])
            print("image_url is " + p['image_url'])
            print("web_url is " + p['web_url'])


        # product_names = [p['name'] for p in extracted_data]
        # print(product_names)
        # Dropdown to select product
        product_name_sel = int(input("Enter the prod number you want"))
        product_names = products[product_name_sel-1]
        #   print(product_names)
        print("name of the product is " + extracted_data[product_name_sel-1]['name'])


        # product_dropdown = gr.Dropdown(label="Select Product", choices=product_names)

        tone = int(input("Enter the tone you want 1 -> simple and 2 -> deeper"))
        if tone == 1:
            tone = "simple"
        else:
            tone = "deeper"
        print(tone)
        
        summ = self.LLM(product_names,tone)
        print(summ)

        

if __name__ == "__main__":
    
    OFF = OpenFoodFacts()
    prod_name = input("Enter the product name: ")
    data = OFF.interface(prod_name)
