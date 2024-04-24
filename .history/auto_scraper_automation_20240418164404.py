import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        titles = [a.text.strip() for a in soup.find_all('a', class_='title')]

        paragraphs = [p.text.strip() for p in soup.find_all('p')]

        return titles, paragraphs
    else:
        print("Error: Failed to retrieve data from the website.")
        return [], []

url = "https://example.com"
titles, paragraphs = scrape_website(url)

print("Titles:")
for title in titles
    print("-", title)

print("\nParagraphs:")
for paragraph in paragraphs:
    print("-", paragraph)
