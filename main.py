import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.flipkart.com/search?q=laptops"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9'
}

try:
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    product_names = []
    product_prices = []

    # Strategy: Find all divs that contain a price symbol '₹'
    # This is more reliable than using class names like 'NxW7LS'
    all_containers = soup.find_all('div', attrs={'data-id': True})

    for container in all_containers:
        # Find the title (usually in a div with a specific class or alt text in img)
        name_tag = container.find('img', alt=True)
        # Find the price (searching for the ₹ symbol)
        price_tag = container.find('div', string=lambda x: x and '₹' in x)

        if name_tag and price_tag:
            product_names.append(name_tag['alt'])
            product_prices.append(price_tag.text)

    if product_names:
        df = pd.DataFrame({"Product Name": product_names, "Price": product_prices})
        df.to_excel("Flipkart_Data.xlsx", index=False)
        print(f"✅ Success! Found {len(product_names)} items and saved to Excel.")
    else:
        print("❌ Still no data. Flipkart is blocking 'requests'.")
        print("Try opening this in your browser: https://www.flipkart.com/search?q=laptops")

except Exception as e:
    print(f"Error: {e}")