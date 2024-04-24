import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the webpage
            soup = BeautifulSoup(response.text, 'html.parser')

            # Example: Extract title of the webpage
            title = soup.title.text
            print("Title:", title)

            # Example: Extract all hyperlinks (anchor tags)
            links = soup.find_all('a')
            for link in links:
                print("Link:", link.get('href'))

            # Return True to indicate successful scraping
            return True
        else:
            print("Failed to retrieve webpage. Status code:", response.status_code)
            return False
    except Exception as e:
        print("Error:", e)
        return False

# Example usage:
url = 'https://example.com'
scrape_website(url)
