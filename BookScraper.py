import requests
from bs4 import BeautifulSoup

try:
    # Send request
    url = "http://books.toscrape.com/catalogue/category/books_1/index.html"
    headers = {'User-Agent': 'Mozilla/5.0'}  # Basic user agent to avoid potential blocking
    response = requests.get(url, headers=headers, timeout=10)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        books = soup.find_all('article', class_='product_pod')

        for book in books:
            try:
                # Extract title
                title = book.h3.a['title']

                # Extract price
                price = book.find('p', class_='price_color').text

                # Extract rating (from class name of p.star-rating)
                rating_element = book.find('p', class_='star-rating')
                rating = rating_element['class'][1]  # Gets number like 'Three', 'Four', etc.

                print(f"Title: {title}")
                print(f"Price: {price}")
                print(f"Rating: {rating} stars")
                print("-" * 50)

            except AttributeError as e:
                print(f"Error processing a book: {e}")
                continue

    else:
        print(f"Failed to retrieve webpage. Status code: {response.status_code}")

except requests.RequestException as e:
    print(f"Error fetching the webpage: {e}")