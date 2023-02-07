import requests
from bs4 import BeautifulSoup
import csv

HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})
# URL of the Amazon product listing page
# page = 2
# url = 'https://www.amazon.in/s?k=bags&page='+str(page)+'&crid=2M096C61O4MLT&qid=1675369232&sprefix=ba%2Caps%2C283&ref=sr_pg_'+str(page)
# # Send a GET request to the URL
# HEADERS = ({"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
#     )
# response = requests.get(url,headers=HEADERS)

# # Parse the HTML content of the page
# soup = BeautifulSoup(response.content, 'html.parser')
# product_cards = soup.find_all('div', class_='a-section a-spacing-small a-spacing-top-small')

# print((product_cards))
# product_name = product_cards.find('span', class_='a-size-medium a-color-base a-text-normal')
# print(product_name)
# Create a CSV file to store the information
# pages = int(input("Enter number of pages to scrape: "))
with open('amazon_bags.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # Write the header row to the CSV file
    writer.writerow(['Product Name', 'URL', 'Price(Rs.)', 'Rating(Out of 5 stars)', 'Number of Reviews'])
    for page in range(1,21):
        url = 'https://www.amazon.in/s?k=bags&page='+str(page)+'&crid=2M096C61O4MLT&qid=1675369232&sprefix=ba%2Caps%2C283&ref=sr_pg_'+str(page)
        # Send a GET request to the URL
        response = requests.get(url,headers=HEADERS)
        
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')
        product_cards = soup.find_all('div', class_='a-section a-spacing-small a-spacing-top-small')
        # Find all the product cards on the page
        product_cards = soup.find_all('div', class_='a-section a-spacing-small a-spacing-top-small')
        amazon = 'https://www.amazon.in'
        # Loop through each product card
        for product_card in product_cards:
            # Extract the product name
            product_name = product_card.find('span', class_='a-size-medium a-color-base a-text-normal')
            if str(type(product_name)) != "<class 'NoneType'>":
                product_name = product_name.text
    
            # Extract the URL of the product
            product_url = product_card.find('a', class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal', href = True)
            if str(type(product_url)) != "<class 'NoneType'>":
                product_url = product_url['href']
                product_url = amazon+product_url
            # Extract the price of the product
            price = product_card.find('span', class_='a-price-whole')
            if str(type(price)) != "<class 'NoneType'>":
                price = price.text
    
            # Extract the rating of the product
            rating = product_card.find('span', class_='a-icon-alt')
            if str(type(rating)) != "<class 'NoneType'>":
                rating = rating.text
                rating = float(rating[0:3])
    
            # Extract the number of reviews of the product
            reviews = product_card.find('span', class_='a-size-base s-underline-text')
            if str(type(reviews)) != "<class 'NoneType'>":
                reviews = reviews.text
                c = reviews.find(',')
                if c != -1:
                    try:
                        reviews = abs(int(reviews.replace(',', '')))
                    except:
                        reviews = reviews.replace('(','').replace(')','') 
                        reviews = abs(int(reviews.replace(',', '')))
                else:
                    try:
                        reviews = abs(int(reviews))
                    except:
                        reviews = reviews.replace('(','').replace(')','') 
                        reviews = abs(int(reviews))
    
            # Write the information to the CSV file
            writer.writerow([product_name, product_url, price, rating, reviews])
