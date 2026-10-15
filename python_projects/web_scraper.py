import requests
import csv
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"

try:
    response = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=15
    )
    response.raise_for_status()
    
except requests.RequestException as error:
    print(f"Error fetching website: {error}")
    raise SystemExit(1)

soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all("div", class_="quote")

scraped_data = []

for quote in quotes:
    text = quote.find("span", class_="text").get_text(strip=True)
    author = quote.find("small", class_="author").get_text(strip=True)
    
    tags = [
        tag.get_text(strip=True)
        for tag in quote.find_all("a", class_="tag")
    ]
    
    scraped_data.append({
        "Quote": text,
        "Author": author,
        "Tags": ", ".join(tags)
    })
    
if scraped_data:
    with open("quotes.csv", "w", newline="", encoding="utf-8") as file:
        fieldnames = ["Quote", "Author", "Tags"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerows(scraped_data)
    
    print(f"Successfully scraped {len(scraped_data)} quotes!")
    print("Data saved to quotes.csv")
    
    for item in scraped_data:
        print(f"\nQuote: {item['Quote']}")
        print(f"Author: {item['Author']}")
        print(f"Tags: {item['Tags']}")
else:
    print("No quotes found. The website structure may have changed.")
