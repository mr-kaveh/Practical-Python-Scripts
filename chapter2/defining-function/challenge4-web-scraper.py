# Python code example that defines a function to perform a web scraping task using the BeautifulSoup library. 
# In this example, we'll scrape and display information from a website, counting the number of headlines in a specified category:

import requests
from bs4 import BeautifulSoup

# Define a function to scrape and count headlines in a specified category
def count_headlines(category_url):
    try:
        # Send an HTTP GET request to the website
        response = requests.get(category_url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content of the page using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find and count the headlines in the specified category
            headlines = soup.find_all('h2', class_='headline')  # Customize the HTML element and class
            num_headlines = len(headlines)

            # Display the headlines and count
            print(f"Headlines in the specified category ({category_url}):")
            for i, headline in enumerate(headlines, 1):
                print(f"{i}. {headline.text.strip()}")
            print(f"Total headlines in this category: {num_headlines}")
        else:
            print("Failed to retrieve the web page.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage: Count headlines in a specific category
category_url = "https://example.com/news/category/politics"
count_headlines(category_url)
