# # -*- coding: utf-8 -*-
# """
# Created on Fri Feb  3 05:22:45 2023

# @author: User
# """

import csv
import requests
from bs4 import BeautifulSoup
# import re



# def scrape_product_info(url):
#     #url = 'https://www.amazon.in/sspa/click?ie=UTF8&spc=MTo3Nzc4Mjc5NjU4ODMwODQyOjE2NzUzODA5NzA6c3BfbXRmOjIwMDkxNzAyMDkzMTk4OjowOjo&url=%2FChris-Kate-Navy-Red-Comfortable-Backpack%2Fdp%2FB0BKWF2Q38%2Fref%3Dsr_1_310_sspa%3Fcrid%3D2M096C61O4MLT%26keywords%3Dbags%26qid%3D1675380970%26sprefix%3Dba%252Caps%252C283%26sr%3D8-310-spons%26sp_csd%3Dd2lkZ2V0TmFtZT1zcF9tdGY%26psc%3D1'
#     # Send a GET request to the URL
#     HEADERS = ({'User-Agent':
#             'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
#             'Accept-Language': 'en-US, en;q=0.5'})
#     response = requests.get(url,headers=HEADERS)
#     print(response.status_code)
#     # Check if the request was successful
#     if response.status_code == 200:
#         # Parse the HTML content of the page
#         soup = BeautifulSoup(response.content, "html.parser")
#         # Find the product name
#         product_name = soup.find("span", id="productTitle").text.strip()
#         #print(product_name)
#         # Find the product description
#         product_desc = soup.find("div", id="feature-bullets").text.strip()
#         #print(product_desc)
#         # Find the ASIN and manufacturer
#         #detailBullets_feature_div
#         data1 = soup.find("div", id= "detailBullets_feature_div").text
#         #print(data1.split())
#         val = data1.split()

#         out1 = int(val.index('ASIN')) + 4
#         if 'Manufucterer' in val:
#             out2 = int(val.index('Manufacturer') + 4)
#             manufacturer = val[out2]
#         else:
#             manufacturer = 'nAn'
#         #print(out2)
#         # print(out)
#         # print(type(data1))
#         ASIN = val[out1]
#         print ( product_desc, ASIN, manufacturer)
#         return (product_name, product_desc, ASIN, manufacturer)


# #preprocessing
import pandas as pd
df = pd.read_csv("amazon_bags.csv",usecols=['URL'])
#dg = pd.read_csv("amazon_bag1.csv")
df.to_csv("prod_urls.csv", index = 'False')

# # Read the URLs from the CSV file


with open("prod_urls.csv", "r") as file:
    reader = csv.reader(file)
    # Open the CSV file to store the product information
    with open("product_info.csv", "w", newline="") as output_file:
        writer = csv.writer(output_file)
        # Write the header row to the CSV file
        writer.writerow(["Product Name","Product Description", "ASIN", "Manufacturer"])
        HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})
        for row in reader:
            if row[1]== 'nan':
                continue
            else:
                url = row[1]
                url = 'http://'+ str(url)
                response = requests.get(url,headers=HEADERS)
                # Check if the request was successful
                if response.status_code == 200:
                    # Parse the HTML content of the page
                    soup = BeautifulSoup(response.content, "html.parser")
                    # Find the product name
                    product_name = soup.find("span", id="productTitle").text.strip()
                    #print(product_name)
                    # Find the product description
                    product_desc = soup.find("div", id="feature-bullets").text.strip()
                    #print(product_desc)
                    # Find the ASIN and manufacturer
                    #detailBullets_feature_div
                    data1 = soup.find("div", id= "detailBullets_feature_div").text
                    #print(data1.split())
                    val = data1.split()
            
                    out1 = int(val.index('ASIN')) + 4
                    if 'Manufacturer' in val:
                        out2 = int(val.index('Manufacturer') + 4)
                        manufacturer = val[out2]
                    else:
                        manufacturer = 'nAn'
                    #print(out2)
                    # print(out)
                    # print(type(data1))
                    ASIN = val[out1]
                # Write the product information to the CSV file
                writer.writerow(product_name, product_desc, ASIN, manufacturer)
